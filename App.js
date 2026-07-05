import React, { useState, useEffect } from 'react';
import {
  View,
  Text,
  TextInput,
  TouchableOpacity,
  FlatList,
  StyleSheet,
  ScrollView,
  Alert,
  ActivityIndicator
} from 'react-native';
import axios from 'axios';

const API_URL = 'http://192.168.1.45:5000/api';

export default function App() {
  const [iller, setIller] = useState([]);
  const [seciliSol, setSeciliSol] = useState(null);
  const [seciliSag, setSeciliSag] = useState(null);
  const [aramaSol, setAramaSol] = useState('');
  const [aramaSag, setAramaSag] = useState('');
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    fetchData();
  }, []);

  const fetchData = async () => {
    setLoading(true);
    try {
      const response = await axios.get(`${API_URL}/iller`);
      setIller(response.data);
    } catch (error) {
      Alert.alert('Hata', 'Veriler yüklenemedi!');
    } finally {
      setLoading(false);
    }
  };

  const selectIl = (il, taraf) => {
    if (il.status === 'eslesti') {
      Alert.alert('Uyarı', 'Bu il zaten eşleşti!');
      return;
    }
    if (taraf === 'sol') {
      setSeciliSol(seciliSol?.id === il.id ? null : il);
    } else {
      setSeciliSag(seciliSag?.id === il.id ? null : il);
    }
  };

  const eslesmeYap = async () => {
    if (!seciliSol || !seciliSag) {
      Alert.alert('Uyarı', 'Lütfen bir sol ve bir sağ il seçin!');
      return;
    }
    try {
      const response = await axios.post(`${API_URL}/esles`, {
        sol_il_id: seciliSol.id,
        sag_il_id: seciliSag.id
      });
      if (response.data.success) {
        Alert.alert('Başarılı', `${seciliSol.name} - ${seciliSag.name} eşleşti!`);
        setSeciliSol(null);
        setSeciliSag(null);
        fetchData();
      }
    } catch (error) {
      Alert.alert('Hata', 'Eşleştirme yapılamadı!');
    }
  };

  const rastgeleEsles = async () => {
    try {
      const response = await axios.post(`${API_URL}/rastgele`);
      if (response.data.success) {
        Alert.alert('Başarılı', `${response.data.eslesmeler.length} çift eşleşti!`);
        fetchData();
      }
    } catch (error) {
      Alert.alert('Hata', 'Rastgele eşleştirme yapılamadı!');
    }
  };

  const ornekEkle = async () => {
    try {
      const response = await axios.post(`${API_URL}/ornek`);
      if (response.data.success) {
        Alert.alert('Başarılı', 'Örnek veriler eklendi!');
        fetchData();
      }
    } catch (error) {
      Alert.alert('Hata', 'Örnek veri eklenemedi!');
    }
  };

  const temizle = async () => {
    Alert.alert('Temizle', 'Tüm veriler silinecek. Devam et?', [
      { text: 'İptal', style: 'cancel' },
      {
        text: 'Temizle',
        style: 'destructive',
        onPress: async () => {
          try {
            await axios.post(`${API_URL}/temizle`);
            Alert.alert('Başarılı', 'Tüm veriler temizlendi!');
            setSeciliSol(null);
            setSeciliSag(null);
            fetchData();
          } catch (error) {
            Alert.alert('Hata', 'Temizleme yapılamadı!');
          }
        }
      }
    ]);
  };

  const renderIl = ({ item, taraf }) => {
    const isSelected = (taraf === 'sol' && seciliSol?.id === item.id) ||
                      (taraf === 'sag' && seciliSag?.id === item.id);
    const isMatched = item.status === 'eslesti';

    return (
      <TouchableOpacity
        style={[
          styles.ilCard,
          isSelected && styles.selectedCard,
          isMatched && styles.matchedCard
        ]}
        onPress={() => selectIl(item, taraf)}
        disabled={isMatched}
      >
        <Text style={styles.ilId}>{String(item.id).padStart(2, '0')}</Text>
        <Text style={styles.ilName}>{item.name}</Text>
        {isMatched && (
          <Text style={styles.matchedText}>❤️ {item.eslesen}</Text>
        )}
        {!isMatched && item.status === 'waiting' && (
          <Text style={styles.waitingText}>⏳ Bekliyor</Text>
        )}
      </TouchableOpacity>
    );
  };

  return (
    <View style={styles.container}>
      <ScrollView>
        <View style={styles.header}>
          <Text style={styles.headerTitle}>Çift Taraflı Eşleştirme</Text>
          <View style={styles.headerStats}>
            <Text style={styles.statText}>81 il</Text>
            <Text style={styles.statText}>
              {iller.filter(i => i.status === 'eslesti').length} Eşleşti
            </Text>
            <Text style={styles.statText}>
              {iller.filter(i => i.status === 'waiting').length} Bekliyor
            </Text>
          </View>
        </View>

        {loading ? (
          <ActivityIndicator size="large" color="#4A90E2" style={styles.loader} />
        ) : (
          <>
            <View style={styles.tarafContainer}>
              <View style={styles.tarafHeader}>
                <Text style={styles.tarafTitle}>⬅️ SOL - VARİŞ YERİ</Text>
                <Text style={styles.tarafCount}>
                  {iller.filter(i => i.taraf === 'sol' && i.status !== 'eslesti').length}/{iller.filter(i => i.taraf === 'sol').length}
                </Text>
              </View>
              
              <TextInput
                style={styles.searchInput}
                placeholder="🔍 İl ara..."
                value={aramaSol}
                onChangeText={setAramaSol}
                blurOnSubmit={false}
              />

              <FlatList
                data={iller.filter(i => 
                  i.taraf === 'sol' && 
                  i.name.toLowerCase().includes(aramaSol.toLowerCase())
                )}
                keyExtractor={(item) => `sol-${item.id}`}
                renderItem={({ item }) => renderIl({ item, taraf: 'sol' })}
                scrollEnabled={false}
                numColumns={3}
              />
            </View>

            <View style={styles.actionContainer}>
              <TouchableOpacity
                style={[styles.actionButton, styles.matchButton]}
                onPress={eslesmeYap}
              >
                <Text style={styles.actionButtonText}>EŞLEŞTİR</Text>
              </TouchableOpacity>

              <TouchableOpacity
                style={[styles.actionButton, styles.randomButton]}
                onPress={rastgeleEsles}
              >
                <Text style={styles.actionButtonText}>RASTGELE</Text>
              </TouchableOpacity>
            </View>

            <View style={styles.actionContainer}>
              <TouchableOpacity
                style={[styles.actionButton, styles.exampleButton]}
                onPress={ornekEkle}
              >
                <Text style={styles.actionButtonText}>ÖRNEK</Text>
              </TouchableOpacity>

              <TouchableOpacity
                style={[styles.actionButton, styles.clearButton]}
                onPress={temizle}
              >
                <Text style={styles.actionButtonText}>TEMİZLE</Text>
              </TouchableOpacity>
            </View>

            <View style={styles.waitingInfo}>
              <Text style={styles.waitingInfoText}>
                ⏳ {iller.filter(i => i.status === 'waiting').length} il bekliyor...
              </Text>
            </View>

            <View style={styles.tarafContainer}>
              <View style={styles.tarafHeader}>
                <Text style={styles.tarafTitle}>➡️ SAĞ - VARİŞ YERİ</Text>
                <Text style={styles.tarafCount}>
                  {iller.filter(i => i.taraf === 'sag' && i.status !== 'eslesti').length}/{iller.filter(i => i.taraf === 'sag').length}
                </Text>
              </View>

              <TextInput
                style={styles.searchInput}
                placeholder="🔍 İl ara..."
                value={aramaSag}
                onChangeText={setAramaSag}
                blurOnSubmit={false}
              />

              <FlatList
                data={iller.filter(i => 
                  i.taraf === 'sag' && 
                  i.name.toLowerCase().includes(aramaSag.toLowerCase())
                )}
                keyExtractor={(item) => `sag-${item.id}`}
                renderItem={({ item }) => renderIl({ item, taraf: 'sag' })}
                scrollEnabled={false}
                numColumns={3}
              />
            </View>
          </>
        )}
      </ScrollView>
    </View>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: '#f5f5f5' },
  header: { backgroundColor: '#4A90E2', padding: 16, paddingTop: 40 },
  headerTitle: { fontSize: 20, fontWeight: 'bold', color: 'white', textAlign: 'center', marginBottom: 8 },
  headerStats: { flexDirection: 'row', justifyContent: 'space-around' },
  statText: { color: 'white', fontSize: 14, fontWeight: '500' },
  loader: { marginTop: 50 },
  tarafContainer: { backgroundColor: 'white', margin: 10, padding: 10, borderRadius: 10, elevation: 2 },
  tarafHeader: { flexDirection: 'row', justifyContent: 'space-between', alignItems: 'center', paddingHorizontal: 8, paddingBottom: 8, borderBottomWidth: 1, borderBottomColor: '#eee' },
  tarafTitle: { fontSize: 16, fontWeight: 'bold', color: '#333' },
  tarafCount: { fontSize: 14, color: '#666' },
  searchInput: { backgroundColor: '#f5f5f5', marginVertical: 8, padding: 10, borderRadius: 8, fontSize: 14 },
  ilCard: { flex: 1, margin: 4, padding: 8, backgroundColor: '#fafafa', borderRadius: 8, borderWidth: 1, borderColor: '#eee', alignItems: 'center', minHeight: 60 },
  selectedCard: { borderColor: '#4A90E2', borderWidth: 2, backgroundColor: '#E3F2FD' },
  matchedCard: { backgroundColor: '#E8F5E9', borderColor: '#4CAF50' },
  ilId: { fontSize: 10, color: '#999' },
  ilName: { fontSize: 13, fontWeight: '600', color: '#333', textAlign: 'center' },
  matchedText: { fontSize: 10, color: '#4CAF50', marginTop: 2 },
  waitingText: { fontSize: 10, color: '#FF9800', marginTop: 2 },
  actionContainer: { flexDirection: 'row', justifyContent: 'space-around', marginHorizontal: 10, marginBottom: 6 },
  actionButton: { flexDirection: 'row', alignItems: 'center', justifyContent: 'center', paddingVertical: 10, paddingHorizontal: 20, borderRadius: 8, flex: 1, marginHorizontal: 4 },
  matchButton: { backgroundColor: '#4CAF50' },
  randomButton: { backgroundColor: '#FF9800' },
  exampleButton: { backgroundColor: '#9C27B0' },
  clearButton: { backgroundColor: '#F44336' },
  actionButtonText: { color: 'white', fontWeight: 'bold', fontSize: 14, marginLeft: 6 },
  waitingInfo: { backgroundColor: '#FFF3E0', marginHorizontal: 10, padding: 8, borderRadius: 8, alignItems: 'center' },
  waitingInfoText: { color: '#E65100', fontWeight: 'bold' },
});
