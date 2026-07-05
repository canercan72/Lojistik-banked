from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)

# 81 il
iller = []
for i in range(1, 82):
    taraf = "sol" if i <= 40 else "sag"
    iller.append({
        "id": i,
        "name": f"İl_{i}",
        "status": "waiting" if i <= 5 else "empty",
        "eslesen": None,
        "taraf": taraf
    })

# Örnek iller
ornek_iller = [
    {"id": 1, "name": "Adana", "status": "waiting", "eslesen": None, "taraf": "sol"},
    {"id": 2, "name": "Adıyaman", "status": "waiting", "eslesen": None, "taraf": "sol"},
    {"id": 3, "name": "Afyonkarahisar", "status": "empty", "eslesen": None, "taraf": "sol"},
    {"id": 4, "name": "Ağrı", "status": "empty", "eslesen": None, "taraf": "sol"},
    {"id": 5, "name": "Aksaray", "status": "empty", "eslesen": None, "taraf": "sol"},
    {"id": 6, "name": "Amasya", "status": "empty", "eslesen": None, "taraf": "sol"},
    {"id": 7, "name": "Ankara", "status": "empty", "eslesen": None, "taraf": "sag"},
    {"id": 8, "name": "Antalya", "status": "empty", "eslesen": None, "taraf": "sag"},
    {"id": 9, "name": "Artvin", "status": "empty", "eslesen": None, "taraf": "sag"},
    {"id": 10, "name": "Aydın", "status": "empty", "eslesen": None, "taraf": "sag"},
    {"id": 11, "name": "Balıkesir", "status": "empty", "eslesen": None, "taraf": "sol"},
    {"id": 12, "name": "Bilecik", "status": "empty", "eslesen": None, "taraf": "sol"},
    {"id": 13, "name": "Bingöl", "status": "empty", "eslesen": None, "taraf": "sol"},
    {"id": 14, "name": "Bitlis", "status": "empty", "eslesen": None, "taraf": "sol"},
    {"id": 15, "name": "Bolu", "status": "empty", "eslesen": None, "taraf": "sol"},
    {"id": 16, "name": "Burdur", "status": "empty", "eslesen": None, "taraf": "sol"},
    {"id": 17, "name": "Bursa", "status": "empty", "eslesen": None, "taraf": "sol"},
    {"id": 18, "name": "Çanakkale", "status": "empty", "eslesen": None, "taraf": "sol"},
    {"id": 19, "name": "Çankırı", "status": "empty", "eslesen": None, "taraf": "sol"},
    {"id": 20, "name": "Çorum", "status": "empty", "eslesen": None, "taraf": "sol"},
    {"id": 21, "name": "Denizli", "status": "empty", "eslesen": None, "taraf": "sag"},
    {"id": 22, "name": "Diyarbakır", "status": "empty", "eslesen": None, "taraf": "sag"},
    {"id": 23, "name": "Edirne", "status": "empty", "eslesen": None, "taraf": "sag"},
    {"id": 24, "name": "Elazığ", "status": "empty", "eslesen": None, "taraf": "sag"},
    {"id": 25, "name": "Erzincan", "status": "empty", "eslesen": None, "taraf": "sag"},
    {"id": 26, "name": "Erzurum", "status": "empty", "eslesen": None, "taraf": "sag"},
    {"id": 27, "name": "Eskişehir", "status": "empty", "eslesen": None, "taraf": "sag"},
    {"id": 28, "name": "Gaziantep", "status": "empty", "eslesen": None, "taraf": "sag"},
    {"id": 29, "name": "Giresun", "status": "empty", "eslesen": None, "taraf": "sag"},
    {"id": 30, "name": "Gümüşhane", "status": "empty", "eslesen": None, "taraf": "sag"},
    {"id": 31, "name": "Hakkari", "status": "empty", "eslesen": None, "taraf": "sol"},
    {"id": 32, "name": "Hatay", "status": "empty", "eslesen": None, "taraf": "sol"},
    {"id": 33, "name": "Isparta", "status": "empty", "eslesen": None, "taraf": "sol"},
    {"id": 34, "name": "Mersin", "status": "empty", "eslesen": None, "taraf": "sol"},
    {"id": 35, "name": "İstanbul", "status": "empty", "eslesen": None, "taraf": "sol"},
    {"id": 36, "name": "İzmir", "status": "empty", "eslesen": None, "taraf": "sol"},
    {"id": 37, "name": "Kars", "status": "empty", "eslesen": None, "taraf": "sol"},
    {"id": 38, "name": "Kastamonu", "status": "empty", "eslesen": None, "taraf": "sol"},
    {"id": 39, "name": "Kayseri", "status": "empty", "eslesen": None, "taraf": "sol"},
    {"id": 40, "name": "Kırklareli", "status": "empty", "eslesen": None, "taraf": "sol"},
    {"id": 41, "name": "Kırşehir", "status": "empty", "eslesen": None, "taraf": "sag"},
    {"id": 42, "name": "Kocaeli", "status": "empty", "eslesen": None, "taraf": "sag"},
    {"id": 43, "name": "Konya", "status": "empty", "eslesen": None, "taraf": "sag"},
    {"id": 44, "name": "Kütahya", "status": "empty", "eslesen": None, "taraf": "sag"},
    {"id": 45, "name": "Malatya", "status": "empty", "eslesen": None, "taraf": "sag"},
    {"id": 46, "name": "Manisa", "status": "empty", "eslesen": None, "taraf": "sag"},
    {"id": 47, "name": "Kahramanmaraş", "status": "empty", "eslesen": None, "taraf": "sag"},
    {"id": 48, "name": "Mardin", "status": "empty", "eslesen": None, "taraf": "sag"},
    {"id": 49, "name": "Muğla", "status": "empty", "eslesen": None, "taraf": "sag"},
    {"id": 50, "name": "Muş", "status": "empty", "eslesen": None, "taraf": "sag"},
    {"id": 51, "name": "Nevşehir", "status": "empty", "eslesen": None, "taraf": "sol"},
    {"id": 52, "name": "Niğde", "status": "empty", "eslesen": None, "taraf": "sol"},
    {"id": 53, "name": "Ordu", "status": "empty", "eslesen": None, "taraf": "sol"},
    {"id": 54, "name": "Rize", "status": "empty", "eslesen": None, "taraf": "sol"},
    {"id": 55, "name": "Sakarya", "status": "empty", "eslesen": None, "taraf": "sol"},
    {"id": 56, "name": "Samsun", "status": "empty", "eslesen": None, "taraf": "sol"},
    {"id": 57, "name": "Siirt", "status": "empty", "eslesen": None, "taraf": "sol"},
    {"id": 58, "name": "Sinop", "status": "empty", "eslesen": None, "taraf": "sol"},
    {"id": 59, "name": "Sivas", "status": "empty", "eslesen": None, "taraf": "sol"},
    {"id": 60, "name": "Tekirdağ", "status": "empty", "eslesen": None, "taraf": "sol"},
    {"id": 61, "name": "Tokat", "status": "empty", "eslesen": None, "taraf": "sag"},
    {"id": 62, "name": "Trabzon", "status": "empty", "eslesen": None, "taraf": "sag"},
    {"id": 63, "name": "Tunceli", "status": "empty", "eslesen": None, "taraf": "sag"},
    {"id": 64, "name": "Şanlıurfa", "status": "empty", "eslesen": None, "taraf": "sag"},
    {"id": 65, "name": "Uşak", "status": "empty", "eslesen": None, "taraf": "sag"},
    {"id": 66, "name": "Van", "status": "empty", "eslesen": None, "taraf": "sag"},
    {"id": 67, "name": "Yozgat", "status": "empty", "eslesen": None, "taraf": "sag"},
    {"id": 68, "name": "Zonguldak", "status": "empty", "eslesen": None, "taraf": "sag"},
    {"id": 69, "name": "Aksaray", "status": "empty", "eslesen": None, "taraf": "sag"},
    {"id": 70, "name": "Bayburt", "status": "empty", "eslesen": None, "taraf": "sag"},
    {"id": 71, "name": "Karaman", "status": "empty", "eslesen": None, "taraf": "sol"},
    {"id": 72, "name": "Kırıkkale", "status": "empty", "eslesen": None, "taraf": "sol"},
    {"id": 73, "name": "Batman", "status": "empty", "eslesen": None, "taraf": "sol"},
    {"id": 74, "name": "Şırnak", "status": "empty", "eslesen": None, "taraf": "sol"},
    {"id": 75, "name": "Bartın", "status": "empty", "eslesen": None, "taraf": "sol"},
    {"id": 76, "name": "Ardahan", "status": "empty", "eslesen": None, "taraf": "sol"},
    {"id": 77, "name": "Iğdır", "status": "empty", "eslesen": None, "taraf": "sol"},
    {"id": 78, "name": "Yalova", "status": "empty", "eslesen": None, "taraf": "sol"},
    {"id": 79, "name": "Karabük", "status": "empty", "eslesen": None, "taraf": "sol"},
    {"id": 80, "name": "Kilis", "status": "empty", "eslesen": None, "taraf": "sol"},
    {"id": 81, "name": "Osmaniye", "status": "empty", "eslesen": None, "taraf": "sol"},
]

iller = ornek_iller
eslesmeler = []
eslesme_id = 0

@app.route('/api/iller', methods=['GET'])
def get_iller():
    return jsonify(iller)

@app.route('/api/esles', methods=['POST'])
def esles():
    global eslesme_id
    data = request.json
    sol_il_id = data.get('sol_il_id')
    sag_il_id = data.get('sag_il_id')
    
    sol_il = next((i for i in iller if i['id'] == sol_il_id and i['taraf'] == 'sol'), None)
    sag_il = next((i for i in iller if i['id'] == sag_il_id and i['taraf'] == 'sag'), None)
    
    if not sol_il or not sag_il:
        return jsonify({'success': False, 'message': 'İl bulunamadı'}), 404
    
    if sol_il['status'] == 'eslesti' or sag_il['status'] == 'eslesti':
        return jsonify({'success': False, 'message': 'Bu il zaten eşleşti!'}), 400
    
    eslesme_id += 1
    eslesme = {
        'id': eslesme_id,
        'sol_il': sol_il['name'],
        'sol_il_id': sol_il['id'],
        'sag_il': sag_il['name'],
        'sag_il_id': sag_il['id'],
        'tarih': datetime.now().strftime('%d.%m.%Y %H:%M')
    }
    eslesmeler.append(eslesme)
    
    sol_il['status'] = 'eslesti'
    sol_il['eslesen'] = sag_il['name']
    sag_il['status'] = 'eslesti'
    sag_il['eslesen'] = sol_il['name']
    
    return jsonify({'success': True, 'eslesme': eslesme})

@app.route('/api/temizle', methods=['POST'])
def temizle():
    global eslesme_id
    for il in iller:
        il['status'] = 'empty'
        il['eslesen'] = None
    eslesmeler.clear()
    eslesme_id = 0
    return jsonify({'success': True})

@app.route('/api/rastgele', methods=['POST'])
def rastgele_esles():
    global eslesme_id
    sol_bekleyen = [i for i in iller if i['taraf'] == 'sol' and i['status'] == 'waiting']
    sag_bekleyen = [i for i in iller if i['taraf'] == 'sag' and i['status'] == 'waiting']
    
    import random
    eslesenler = []
    
    while sol_bekleyen and sag_bekleyen:
        sol = random.choice(sol_bekleyen)
        sag = random.choice(sag_bekleyen)
        
        eslesme_id += 1
        eslesme = {
            'id': eslesme_id,
            'sol_il': sol['name'],
            'sol_il_id': sol['id'],
            'sag_il': sag['name'],
            'sag_il_id': sag['id'],
            'tarih': datetime.now().strftime('%d.%m.%Y %H:%M')
        }
        eslesmeler.append(eslesme)
        
        sol['status'] = 'eslesti'
        sol['eslesen'] = sag['name']
        sag['status'] = 'eslesti'
        sag['eslesen'] = sol['name']
        
        sol_bekleyen.remove(sol)
        sag_bekleyen.remove(sag)
        eslesenler.append(eslesme)
    
    return jsonify({'success': True, 'eslesmeler': eslesenler})

@app.route('/api/ornek', methods=['POST'])
def ornek_veri():
    global eslesme_id
    ornek_eslesmeler = [
        {'sol': 'Adana', 'sag': 'Ankara'},
        {'sol': 'Adıyaman', 'sag': 'Antalya'},
        {'sol': 'Afyonkarahisar', 'sag': 'Aydın'}
    ]
    
    for es in ornek_eslesmeler:
        sol = next((i for i in iller if i['name'] == es['sol'] and i['taraf'] == 'sol'), None)
        sag = next((i for i in iller if i['name'] == es['sag'] and i['taraf'] == 'sag'), None)
        
        if sol and sag and sol['status'] != 'eslesti' and sag['status'] != 'eslesti':
            eslesme_id += 1
            eslesme = {
                'id': eslesme_id,
                'sol_il': sol['name'],
                'sol_il_id': sol['id'],
                'sag_il': sag['name'],
                'sag_il_id': sag['id'],
                'tarih': datetime.now().strftime('%d.%m.%Y %H:%M')
            }
            eslesmeler.append(eslesme)
            
            sol['status'] = 'eslesti'
            sol['eslesen'] = sag['name']
            sag['status'] = 'eslesti'
            sag['eslesen'] = sol['name']
    
    return jsonify({'success': True})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
