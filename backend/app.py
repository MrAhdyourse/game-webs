from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app) # Mengizinkan CORS untuk pengembangan frontend

# Contoh data cerita (akan diperluas nanti)
# Dalam aplikasi nyata, ini bisa diambil dari database
story_data = {
    "start": {
        "text": "Anda terbangun di tengah hutan lebat yang belum pernah Anda lihat sebelumnya. Kabut tipis menyelimuti pepohonan tinggi. Ada dua jalan di depan Anda.",
        "choices": [
            {"text": "Ambil jalan setapak ke kiri.", "next": "left_path"},
            {"text": "Ambil jalan setapak ke kanan.", "next": "right_path"}
        ]
    },
    "left_path": {
        "text": "Anda mengikuti jalan setapak ke kiri. Suara gemericik air terdengar di kejauhan. Anda menemukan sebuah sungai kecil.",
        "choices": [
            {"text": "Menyeberangi sungai.", "next": "cross_river"},
            {"text": "Mencari jalan memutar.", "next": "find_detour"}
        ]
    },
    "right_path": {
        "text": "Anda mengambil jalan ke kanan. Semakin dalam Anda melangkah, semakin gelap hutan ini. Anda mendengar suara gemerisik di semak-semak.",
        "choices": [
            {"text": "Mendekati sumber suara.", "next": "approach_sound"},
            {"text": "Bersembunyi di balik pohon.", "next": "hide_behind_tree"}
        ]
    },
    "cross_river": {
        "text": "Anda berhasil menyeberangi sungai. Di seberang, Anda melihat sebuah gua.",
        "choices": [
            {"text": "Masuk ke dalam gua.", "next": "enter_cave"},
            {"text": "Melanjutkan perjalanan menyusuri sungai.", "next": "follow_river"}
        ]
    },
    "find_detour": {
        "text": "Anda mencari jalan memutar dan menemukan jembatan kayu tua. Jembatan itu terlihat rapuh.",
        "choices": [
            {"text": "Menyeberangi jembatan.", "next": "cross_bridge"},
            {"text": "Kembali ke sungai dan menyeberanginya.", "next": "cross_river"}
        ]
    },
    "approach_sound": {
        "text": "Anda mendekati sumber suara dan menemukan seekor kelinci hutan yang sedang makan daun. Kelinci itu melarikan diri.",
        "choices": [
            {"text": "Melanjutkan perjalanan.", "next": "continue_journey"}
        ]
    },
    "hide_behind_tree": {
        "text": "Anda bersembunyi di balik pohon. Beberapa saat kemudian, seekor rusa melintas tanpa menyadari keberadaan Anda.",
        "choices": [
            {"text": "Melanjutkan perjalanan.", "next": "continue_journey"}
        ]
    },
    "enter_cave": {
        "text": "Anda masuk ke dalam gua. Gelap gulita. Anda tidak bisa melihat apa-apa.",
        "choices": [
            {"text": "Mencari jalan keluar.", "next": "end_game"}
        ]
    },
    "follow_river": {
        "text": "Anda melanjutkan perjalanan menyusuri sungai. Anda menemukan sebuah desa kecil di tepi sungai.",
        "choices": [
            {"text": "Masuk ke desa.", "next": "enter_village"}
        ]
    },
    "cross_bridge": {
        "text": "Anda berhasil menyeberangi jembatan. Di seberang, Anda melihat sebuah menara tinggi.",
        "choices": [
            {"text": "Mendekati menara.", "next": "approach_tower"}
        ]
    },
    "continue_journey": {
        "text": "Anda melanjutkan perjalanan. Hutan terasa semakin misterius.",
        "choices": [
            {"text": "Mencari tempat berlindung untuk malam ini.", "next": "find_shelter"}
        ]
    },
    "enter_village": {
        "text": "Anda masuk ke desa. Penduduk desa menyambut Anda dengan ramah. Petualangan Anda berakhir di sini untuk saat ini.",
        "choices": [
            {"text": "Mulai lagi.", "next": "start"}
        ]
    },
    "approach_tower": {
        "text": "Anda mendekati menara. Pintu menara terbuka sedikit. Anda bisa mendengar suara aneh dari dalam.",
        "choices": [
            {"text": "Masuk ke menara.", "next": "enter_tower"},
            {"text": "Meninggalkan menara.", "next": "continue_journey"}
        ]
    },
    "find_shelter": {
        "text": "Anda menemukan sebuah gua kecil yang bisa dijadikan tempat berlindung. Anda memutuskan untuk bermalam di sana.",
        "choices": [
            {"text": "Tidur.", "next": "end_game"}
        ]
    },
    "enter_tower": {
        "text": "Anda masuk ke menara. Di dalamnya, Anda menemukan sebuah portal bercahaya. Anda melangkah masuk dan petualangan Anda berlanjut ke dimensi lain!",
        "choices": [
            {"text": "Mulai lagi.", "next": "start"}
        ]
    },
    "end_game": {
        "text": "Petualangan Anda berakhir di sini. Anda bisa memulai lagi.",
        "choices": [
            {"text": "Mulai lagi.", "next": "start"}
        ]
    }
}

@app.route('/api/story/<scene_id>', methods=['GET'])
def get_story_scene(scene_id):
    scene = story_data.get(scene_id)
    if not scene:
        return jsonify({"error": "Scene not found"}), 404
    return jsonify(scene)

if __name__ == '__main__':
    app.run(debug=True, port=5000)