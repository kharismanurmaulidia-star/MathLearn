import streamlit as st
import matplotlib.pyplot as plt
import random

# =========================================================
# KONFIGURASI APLIKASI
# =========================================================
st.set_page_config(
    page_title="MathLearn | Transformasi Geometri",
    page_icon="📐",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# STYLE — TEMA PASTEL MATHLEARN
# =========================================================
st.markdown("""
<style>
    /* Latar halaman */
    .stApp {
        background-color: #FFF9F5;
        color: #514653;
    }

    /* Sidebar pink pastel */
    [data-testid="stSidebar"] {
        background-color: #F5E5ED;
        border-right: 1px solid #EAD2DF;
    }

    [data-testid="stSidebar"] * {
        color: #68485A;
    }

    [data-testid="stSidebar"] hr {
        border-color: #E5C9D9;
    }

    /* Header beranda */
    .hero {
        background: linear-gradient(120deg, #F4DDE8, #E4E0F8);
        padding: 30px;
        border-radius: 20px;
        color: #563F50;
        margin-bottom: 22px;
        border: 1px solid #E5D3E8;
        box-shadow: 0 4px 14px rgba(115, 82, 105, 0.08);
    }

    .hero h1 {
        color: #563F50 !important;
        font-size: 38px;
    }

    .hero p {
        color: #684F68 !important;
        font-size: 17px;
    }

    /* Empat kotak materi */
    .info-card {
        background-color: #F8E8EF;
        padding: 20px;
        border-radius: 16px;
        border: 1px solid #EBCFDA;
        margin-bottom: 14px;
        min-height: 135px;
        box-shadow: 0 3px 10px rgba(115, 82, 105, 0.06);
    }

    .info-card:nth-of-type(even) {
        background-color: #E7F1E8;
        border-color: #D0E3D3;
    }

    .info-card h3 {
        color: #67465A !important;
        font-size: 22px;
    }

    .info-card p {
        color: #5E5660 !important;
        font-size: 15px;
        line-height: 1.6;
    }

    /* Warna judul dan teks */
    h1, h2, h3, h4 {
        color: #67465A;
    }

    [data-testid="stMarkdownContainer"] p,
    [data-testid="stMarkdownContainer"] li {
        color: #514653;
    }

    /* Tombol */
    div.stButton > button,
    div.stFormSubmitButton > button {
        background-color: #EBCBD9;
        color: #563F50 !important;
        border: 1px solid #DDB5C9;
        border-radius: 12px;
        font-weight: 600;
    }

    div.stButton > button p,
    div.stFormSubmitButton > button p {
        color: #563F50 !important;
    }

    div.stButton > button:hover,
    div.stFormSubmitButton > button:hover {
        background-color: #DDB9D0;
        border-color: #C99DB9;
        color: #493044 !important;
    }

    /* Kotak pilihan dan input */
    div[data-baseweb="select"] > div,
    div[data-baseweb="input"] > div,
    div[data-baseweb="textarea"] > div {
        background-color: #FFFFFF;
        border-color: #E2CFDE;
        border-radius: 10px;
    }

    /* Kartu statistik */
    [data-testid="stMetric"] {
        background-color: #F4EAF5;
        border: 1px solid #E5D7EA;
        padding: 16px;
        border-radius: 14px;
    }

    [data-testid="stMetricLabel"] {
        color: #715B76;
    }

    [data-testid="stMetricValue"] {
        color: #62476D;
    }

    /* Progress bar */
    [data-testid="stProgressBar"] > div {
        background-color: #EADDEB;
        border-radius: 20px;
    }

    [data-testid="stProgressBar"] > div > div {
        background-color: #C99DB9;
        border-radius: 20px;
    }

    /* Garis dan teks kecil */
    hr {
        border-color: #EADDE5;
    }

    .small-text,
    .stCaption {
        color: #756779;
        font-size: 14px;
    }

    /* Slider */
    [data-testid="stSlider"] [role="slider"] {
        background-color: #C99DB9;
    }

    /* Link */
    a {
        color: #986783;
    }

    /* Kotak notifikasi */
    [data-testid="stAlert"] {
        border-radius: 12px;
    }
</style>
""", unsafe_allow_html=True)

# =========================================================
# SESSION STATE
# =========================================================
if "completed_materials" not in st.session_state:
    st.session_state.completed_materials = []

if "quiz_score" not in st.session_state:
    st.session_state.quiz_score = None

if "quiz_answers" not in st.session_state:
    st.session_state.quiz_answers = {}

if "quiz_submitted" not in st.session_state:
    st.session_state.quiz_submitted = False

if "game_score" not in st.session_state:
    st.session_state.game_score = 0

if "game_question" not in st.session_state:
    st.session_state.game_question = None

if "game_answered" not in st.session_state:
    st.session_state.game_answered = False

if "game_feedback" not in st.session_state:
    st.session_state.game_feedback = ""

if "game_attempts" not in st.session_state:
    st.session_state.game_attempts = 0

if "game_question_count" not in st.session_state:
    st.session_state.game_question_count = 0

if "game_round_points" not in st.session_state:
    st.session_state.game_round_points = 0

# =========================================================
# DATA MATERI
# =========================================================
materials = {
    "Translasi": {
        "emoji": "➡️",
        "description": "Pergeseran titik atau bangun tanpa mengubah bentuk dan ukurannya.",
        "formula": "(x, y) → (x + a, y + b)",
        "detail": [
            "a > 0: bergeser ke kanan.",
            "a < 0: bergeser ke kiri.",
            "b > 0: bergeser ke atas.",
            "b < 0: bergeser ke bawah."
        ],
        "example": "Titik A(2, 3) ditranslasikan oleh T(4, -2).",
        "solution": [
            "Koordinat awal: A(2, 3).",
            "Vektor translasi: T(4, -2).",
            "Absis bayangan: x' = 2 + 4 = 6.",
            "Ordinat bayangan: y' = 3 + (-2) = 1.",
            "Jadi, bayangan titik A adalah A'(6, 1)."
        ]
    },
    "Refleksi": {
        "emoji": "🪞",
        "description": "Pencerminan titik atau bangun terhadap garis tertentu.",
        "formula": "Terhadap sumbu-X: (x, y) → (x, -y)",
        "detail": [
            "Sumbu-X: (x, y) → (x, -y).",
            "Sumbu-Y: (x, y) → (-x, y).",
            "Titik O: (x, y) → (-x, -y).",
            "Garis y = x: (x, y) → (y, x).",
            "Garis y = -x: (x, y) → (-y, -x)."
        ],
        "example": "Titik B(3, 2) dicerminkan terhadap sumbu-Y.",
        "solution": [
            "Koordinat awal: B(3, 2).",
            "Aturan refleksi sumbu-Y: (x, y) → (-x, y).",
            "Absis bayangan: x' = -3.",
            "Ordinat bayangan: y' = 2.",
            "Jadi, B'(-3, 2)."
        ]
    },
    "Rotasi": {
        "emoji": "🔄",
        "description": "Perputaran titik atau bangun terhadap pusat dan sudut tertentu.",
        "formula": "Pusat O, 90° berlawanan jarum jam: (x, y) → (-y, x)",
        "detail": [
            "90° berlawanan jarum jam: (x, y) → (-y, x).",
            "90° searah jarum jam: (x, y) → (y, -x).",
            "180°: (x, y) → (-x, -y).",
            "Rotasi dilakukan terhadap pusat O(0, 0)."
        ],
        "example": "Titik C(2, 3) dirotasikan 90° berlawanan arah jarum jam.",
        "solution": [
            "Koordinat awal: C(2, 3).",
            "Aturan rotasi 90°: (x, y) → (-y, x).",
            "Koordinat bayangan: (-3, 2).",
            "Jadi, C'(-3, 2)."
        ]
    },
    "Dilatasi": {
        "emoji": "🔍",
        "description": "Perubahan ukuran bangun dengan faktor skala tertentu.",
        "formula": "Pusat O: (x, y) → (kx, ky)",
        "detail": [
            "k > 1: ukuran bayangan membesar.",
            "0 < k < 1: ukuran bayangan mengecil.",
            "k = 1: ukuran tetap.",
            "k < 0: bayangan berada pada arah berlawanan dari pusat O."
        ],
        "example": "Titik D(2, 3) didilatasikan dengan pusat O dan faktor skala 2.",
        "solution": [
            "Koordinat awal: D(2, 3).",
            "Faktor skala: k = 2.",
            "Absis bayangan: x' = 2 × 2 = 4.",
            "Ordinat bayangan: y' = 2 × 3 = 6.",
            "Jadi, D'(4, 6)."
        ]
    }
}

# =========================================================
# SOAL KUIS
# =========================================================
quiz_questions = [
    {
        "question": "Titik A(2, 3) ditranslasikan oleh T(4, -1). Koordinat A' adalah ...",
        "options": ["(6, 2)", "(6, 4)", "(-2, 4)", "(2, 6)"],
        "answer": "(6, 2)",
        "explanation": "x' = 2 + 4 = 6 dan y' = 3 + (-1) = 2. Jadi A'(6, 2)."
    },
    {
        "question": "Bayangan titik B(4, -2) terhadap sumbu-X adalah ...",
        "options": ["(-4, -2)", "(4, 2)", "(-4, 2)", "(2, 4)"],
        "answer": "(4, 2)",
        "explanation": "Refleksi sumbu-X mengubah (x, y) menjadi (x, -y). Jadi B'(4, 2)."
    },
    {
        "question": "Titik C(2, 5) dirotasikan 90° berlawanan arah jarum jam dengan pusat O. Bayangannya adalah ...",
        "options": ["(5, -2)", "(-5, 2)", "(-2, -5)", "(2, -5)"],
        "answer": "(-5, 2)",
        "explanation": "Rotasi 90° berlawanan arah jarum jam menggunakan aturan (x, y) → (-y, x)."
    },
    {
        "question": "Titik D(3, 2) didilatasikan dengan pusat O dan faktor skala 3. Bayangannya adalah ...",
        "options": ["(6, 5)", "(1, 2)", "(9, 6)", "(-9, -6)"],
        "answer": "(9, 6)",
        "explanation": "x' = 3 × 3 = 9 dan y' = 3 × 2 = 6."
    },
    {
        "question": "Transformasi yang mempertahankan bentuk dan ukuran bangun adalah ...",
        "options": ["Dilatasi saja", "Translasi, refleksi, dan rotasi", "Dilatasi dengan semua faktor skala", "Semua dilatasi"],
        "answer": "Translasi, refleksi, dan rotasi",
        "explanation": "Translasi, refleksi, dan rotasi mempertahankan panjang serta besar sudut. Dilatasi mengubah ukuran jika |k| tidak sama dengan 1."
    }
]

# =========================================================
# SIDEBAR DAN NAVIGASI
# =========================================================
with st.sidebar:
    st.markdown("# 📐 MathLearn")
    st.caption("Belajar Matematika Jadi Lebih Mudah")
    st.divider()

    page = st.radio(
        "MENU UTAMA",
        [
            "🏠 Beranda",
            "📚 Materi Interaktif",
            "📊 Visualisasi",
            "📝 Kuis Otomatis",
            "🎮 Game Matematika",
            "📈 Progres Belajar"
        ]
    )

    st.divider()
    st.markdown("**Transformasi Geometri**")
    st.caption("Matematika SMP Kelas IX")
    st.caption("Fase D | Kurikulum Merdeka")

# =========================================================
# FUNGSI VISUALISASI
# =========================================================
def transform_point(x, y, transformation, a=0, b=0, k=2):
    if transformation == "Translasi":
        return x + a, y + b
    elif transformation == "Refleksi terhadap sumbu-X":
        return x, -y
    elif transformation == "Refleksi terhadap sumbu-Y":
        return -x, y
    elif transformation == "Rotasi 90°":
        return -y, x
    elif transformation == "Rotasi 180°":
        return -x, -y
    elif transformation == "Dilatasi":
        return k * x, k * y
    return x, y


def draw_transformation(transformation, a=0, b=0, k=2):
    original = [(1, 1), (4, 1), (2, 3)]
    transformed = [
        transform_point(x, y, transformation, a, b, k)
        for x, y in original
    ]

    fig, ax = plt.subplots(figsize=(8, 6))

    ox = [p[0] for p in original] + [original[0][0]]
    oy = [p[1] for p in original] + [original[0][1]]

    tx = [p[0] for p in transformed] + [transformed[0][0]]
    ty = [p[1] for p in transformed] + [transformed[0][1]]

    ax.plot(ox, oy, marker="o", linewidth=2, label="Bangun awal")
    ax.plot(tx, ty, marker="o", linewidth=2, linestyle="--",
            label="Hasil transformasi")

    for i, point in enumerate(original):
        ax.annotate(
            f"{chr(65+i)}{point}",
            (point[0], point[1]),
            xytext=(5, 7),
            textcoords="offset points"
        )

    for i, point in enumerate(transformed):
        ax.annotate(
            f"{chr(65+i)}'{point}",
            (point[0], point[1]),
            xytext=(5, -14),
            textcoords="offset points"
        )

    ax.axhline(0, linewidth=1)
    ax.axvline(0, linewidth=1)
    ax.set_xlabel("Sumbu X")
    ax.set_ylabel("Sumbu Y")
    ax.set_title("Visualisasi Transformasi Geometri")
    ax.grid(True, alpha=0.3)
    ax.set_aspect("equal", adjustable="datalim")
    ax.legend()
    fig.tight_layout()

    return fig

# =========================================================
# BERANDA
# =========================================================
if page == "🏠 Beranda":
    st.markdown("""
    <div class="hero">
        <h1>Selamat Datang di MathLearn! 👋</h1>
        <p>
        Platform pembelajaran matematika interaktif untuk memahami
        Transformasi Geometri dengan cara yang menyenangkan.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.subheader("✨ Apa yang akan kamu pelajari?")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div class="info-card">
            <h3>➡️ Translasi</h3>
            <p>Memahami pergeseran titik dan bangun pada bidang koordinat.</p>
        </div>
        <div class="info-card">
            <h3>🪞 Refleksi</h3>
            <p>Mempelajari pencerminan terhadap sumbu dan garis tertentu.</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="info-card">
            <h3>🔄 Rotasi</h3>
            <p>Mengeksplorasi perputaran bangun berdasarkan sudut tertentu.</p>
        </div>
        <div class="info-card">
            <h3>🔍 Dilatasi</h3>
            <p>Memahami perubahan ukuran menggunakan faktor skala.</p>
        </div>
        """, unsafe_allow_html=True)

    st.subheader("🚀 Mulai Petualangan Belajarmu")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Materi", "4 topik")

    with col2:
        st.metric("Kuis", f"{len(quiz_questions)} soal")

    with col3:
        st.metric("Game", "Tantangan koordinat")

    st.info(
        "Tips belajar: pelajari konsep terlebih dahulu, "
        "amati visualisasi, lalu uji pemahaman melalui kuis."
    )

    if st.button("📚 Mulai Belajar", use_container_width=True):
        st.session_state["completed_materials"]
        st.success("Pilih menu Materi Interaktif pada sidebar untuk mulai.")

# =========================================================
# MATERI INTERAKTIF
# =========================================================
elif page == "📚 Materi Interaktif":
    st.title("📚 Materi Interaktif")
    st.write(
        "Pelajari konsep, rumus, dan contoh soal Transformasi Geometri."
    )

    selected_material = st.selectbox(
        "Pilih materi yang ingin dipelajari:",
        list(materials.keys())
    )

    data = materials[selected_material]

    st.markdown(f"## {data['emoji']} {selected_material}")
    st.write(data["description"])

    st.markdown("### 📌 Rumus Utama")
    st.latex(data["formula"])

    st.markdown("### 🧠 Hal Penting")
    for detail in data["detail"]:
        st.markdown(f"- {detail}")

    st.divider()

    st.markdown("### ✍️ Contoh Soal")
    st.info(data["example"])

    with st.expander("Lihat pembahasan langkah demi langkah", expanded=True):
        for i, step in enumerate(data["solution"], start=1):
            st.write(f"**Langkah {i}.** {step}")

    if st.button(
        "✅ Tandai Materi Selesai",
        key=f"complete_{selected_material}"
    ):
        if selected_material not in st.session_state.completed_materials:
            st.session_state.completed_materials.append(selected_material)
        st.success(f"Materi {selected_material} berhasil ditandai selesai!")

    st.progress(
        len(st.session_state.completed_materials) / len(materials)
    )
    st.caption(
        f"{len(st.session_state.completed_materials)} dari "
        f"{len(materials)} materi telah selesai."
    )

# =========================================================
# VISUALISASI
# =========================================================
elif page == "📊 Visualisasi":
    st.title("📊 Visualisasi Transformasi Geometri")
    st.write(
        "Ubah parameter transformasi dan amati perubahan posisi "
        "segitiga pada bidang koordinat Kartesius."
    )

    transformation = st.selectbox(
        "Pilih jenis transformasi:",
        [
            "Translasi",
            "Refleksi terhadap sumbu-X",
            "Refleksi terhadap sumbu-Y",
            "Rotasi 90°",
            "Rotasi 180°",
            "Dilatasi"
        ]
    )

    a, b, k = 0, 0, 2

    if transformation == "Translasi":
        col1, col2 = st.columns(2)
        with col1:
            a = st.slider("Pergeseran horizontal (a)", -5, 5, 2)
        with col2:
            b = st.slider("Pergeseran vertikal (b)", -5, 5, 1)

        st.latex(
            rf"(x,y)\rightarrow(x+({a}),y+({b}))"
        )

    elif transformation == "Dilatasi":
        k = st.slider("Faktor skala (k)", -3, 3, 2)
        if k == 0:
            st.warning(
                "Faktor skala 0 memetakan seluruh titik ke pusat O "
                "sehingga bangun menjadi satu titik."
            )
        st.latex(rf"(x,y)\rightarrow({k}x,{k}y)")

    else:
        st.info(f"Transformasi yang dipilih: {transformation}")

    fig = draw_transformation(transformation, a, b, k)
    st.pyplot(fig)
    plt.close(fig)

    st.markdown("### 🔎 Cara Membaca Visualisasi")
    st.markdown("""
    - Garis penuh menunjukkan bangun awal.
    - Garis putus-putus menunjukkan hasil transformasi.
    - Koordinat titik dapat dibandingkan sebelum dan sesudah transformasi.
    - Perhatikan perubahan posisi, arah, dan ukuran bangun.
    """)

# =========================================================
# KUIS OTOMATIS
# =========================================================
elif page == "📝 Kuis Otomatis":
    st.title("📝 Kuis Transformasi Geometri")
    st.write(
        "Jawab lima soal berikut. Pilih satu jawaban untuk setiap soal, "
        "kemudian tekan tombol periksa jawaban."
    )

    with st.form("quiz_form"):
        selected_answers = {}

        for i, question in enumerate(quiz_questions):
            st.markdown(f"### Soal {i+1}")
            st.write(question["question"])

            selected_answers[i] = st.radio(
                f"Pilih jawaban soal {i+1}:",
                question["options"],
                index=None,
                key=f"quiz_{i}"
            )

        submitted = st.form_submit_button(
            "Periksa Jawaban",
            use_container_width=True
        )

    if submitted:
        unanswered = [
            i for i, answer in selected_answers.items()
            if answer is None
        ]

        if unanswered:
            st.warning(
                "Masih ada soal yang belum dijawab: "
                + ", ".join(str(i+1) for i in unanswered)
            )
        else:
            score = sum(
                selected_answers[i] == question["answer"]
                for i, question in enumerate(quiz_questions)
            )

            st.session_state.quiz_score = score * 20
            st.session_state.quiz_answers = selected_answers
            st.session_state.quiz_submitted = True

    if st.session_state.quiz_submitted:
        st.divider()
        score = st.session_state.quiz_score

        st.subheader("📊 Hasil Kuis")
        st.metric("Nilai Akhir", f"{score}/100")

        if score >= 80:
            st.success("Hebat! Pemahamanmu sudah sangat baik.")
        elif score >= 60:
            st.info("Cukup baik. Pelajari kembali soal yang belum tepat.")
        else:
            st.warning(
                "Tetap semangat! Pelajari kembali materi dan pembahasannya."
            )

        for i, question in enumerate(quiz_questions):
            user_answer = st.session_state.quiz_answers[i]
            correct = user_answer == question["answer"]

            if correct:
                st.success(f"Soal {i+1}: Jawaban benar.")
            else:
                st.error(
                    f"Soal {i+1}: Jawabanmu {user_answer}. "
                    f"Jawaban benar: {question['answer']}."
                )

            with st.expander(f"Pembahasan soal {i+1}"):
                st.write(question["explanation"])

        if st.button("🔄 Ulangi Kuis"):
            st.session_state.quiz_submitted = False
            st.session_state.quiz_score = None
            st.session_state.quiz_answers = {}
            st.rerun()

# =========================================================
# GAME EDUKASI
# =========================================================
elif page == "🎮 Game Matematika":
    st.title("🎮 Coordinate Challenge")
    st.write(
        "Tantang dirimu untuk menentukan bayangan titik dengan cepat "
        "dan tepat!"
    )

    st.markdown("### 🏆 Aturan Permainan")
    st.markdown("""
    1. Baca koordinat awal dan jenis transformasinya.
    2. Tentukan koordinat bayangan.
    3. Pilih jawaban yang tepat.
    4. Jawaban benar mendapatkan 10 poin.
    """)

    if st.session_state.game_question is None:
        if st.button("Mulai Tantangan", use_container_width=True):
            transformations = [
                "Translasi",
                "Refleksi terhadap sumbu-X",
                "Refleksi terhadap sumbu-Y",
                "Rotasi 90°",
                "Rotasi 180°",
                "Dilatasi"
            ]

            x = random.randint(-4, 4)
            y = random.randint(-4, 4)
            if x == 0 and y == 0:
                x = 2

            transformation = random.choice(transformations)
            a = random.randint(-3, 3)
            b = random.randint(-3, 3)
            k = random.choice([-2, -1, 1, 2, 3])

            answer = transform_point(x, y, transformation, a, b, k)

            if transformation == "Translasi":
                description = f"T({a}, {b})"
            elif transformation == "Dilatasi":
                description = f"pusat O, faktor skala {k}"
            else:
                description = transformation

            correct_answer = f"({answer[0]}, {answer[1]})"

            options = {correct_answer}
            while len(options) < 4:
                wrong_x = answer[0] + random.choice([-3, -2, -1, 1, 2, 3])
                wrong_y = answer[1] + random.choice([-3, -2, -1, 1, 2, 3])
                options.add(f"({wrong_x}, {wrong_y})")

            st.session_state.game_question = {
                "x": x,
                "y": y,
                "transformation": transformation,
                "description": description,
                "answer": correct_answer,
                "options": sorted(options),
                "a": a,
                "b": b,
                "k": k
            }
            st.session_state.game_answered = False
            st.session_state.game_feedback = ""
            st.rerun()

    if st.session_state.game_question is not None:
        q = st.session_state.game_question

        st.markdown("### ❓ Pertanyaan")
        st.markdown(
            f"Bayangan titik **A({q['x']}, {q['y']})** "
            f"setelah transformasi **{q['description']}** adalah ..."
        )

        game_choice = st.radio(
            "Pilih koordinat bayangan:",
            q["options"],
            key=f"game_choice_{st.session_state.game_question_count}"
        )

        if not st.session_state.game_answered:
            if st.button("Periksa Jawaban", key="check_game"):
                st.session_state.game_attempts += 1
                st.session_state.game_answered = True

                if game_choice == q["answer"]:
                    st.session_state.game_round_points = 10
                    st.session_state.game_score += 10
                    st.session_state.game_feedback = (
                        "Benar! Kamu mendapatkan 10 poin."
                    )
                else:
                    st.session_state.game_round_points = 0
                    st.session_state.game_feedback = (
                        f"Belum tepat. Jawaban yang benar adalah "
                        f"{q['answer']}."
                    )

                st.rerun()

        else:
            if st.session_state.game_round_points == 10:
                st.success(st.session_state.game_feedback)
            else:
                st.error(st.session_state.game_feedback)

            with st.expander("Lihat pembahasan"):
                st.write(
                    f"Koordinat awal: A({q['x']}, {q['y']})."
                )
                st.write(
                    f"Transformasi: {q['description']}."
                )

                result = transform_point(
                    q["x"], q["y"],
                    q["transformation"],
                    q["a"], q["b"], q["k"]
                )

                st.write(
                    f"Koordinat bayangan: A'({result[0]}, {result[1]})."
                )

            if st.button("Soal Berikutnya", key="next_game"):
                st.session_state.game_question = None
                st.session_state.game_answered = False
                st.session_state.game_feedback = ""
                st.session_state.game_round_points = 0
                st.session_state.game_question_count += 1
                st.rerun()

    st.divider()
    col1, col2 = st.columns(2)

    with col1:
        st.metric("Total Poin", st.session_state.game_score)

    with col2:
        st.metric("Percobaan", st.session_state.game_attempts)

    if st.button("Reset Skor Game"):
        st.session_state.game_score = 0
        st.session_state.game_attempts = 0
        st.session_state.game_question = None
        st.session_state.game_answered = False
        st.session_state.game_feedback = ""
        st.session_state.game_question_count = 0
        st.session_state.game_round_points = 0
        st.rerun()

# =========================================================
# PROGRES BELAJAR
# =========================================================
elif page == "📈 Progres Belajar":
    st.title("📈 Progres Belajar")
    st.write(
        "Pantau perkembangan belajarmu selama menggunakan MathLearn."
    )

    completed = len(st.session_state.completed_materials)
    total = len(materials)
    percentage = completed / total

    st.subheader("📚 Penyelesaian Materi")
    st.progress(percentage)
    st.write(f"**{completed}/{total} materi selesai** ({percentage:.0%})")

    for material in materials:
        if material in st.session_state.completed_materials:
            st.success(f"✅ {material}")
        else:
            st.write(f"⬜ {material} — belum selesai")

    st.divider()
    st.subheader("📝 Hasil Kuis")

    if st.session_state.quiz_score is not None:
        st.metric("Nilai Kuis Terakhir", f"{st.session_state.quiz_score}/100")
    else:
        st.info("Kamu belum menyelesaikan kuis.")

    st.divider()
    st.subheader("🎮 Hasil Game")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Total Poin Game", st.session_state.game_score)

    with col2:
        st.metric("Percobaan Game", st.session_state.game_attempts)

    st.caption(
        "Catatan: progres tersimpan selama sesi aplikasi berjalan. "
        "Data dapat kembali ke awal jika sesi direset atau aplikasi dimulai ulang."
    )

# =========================================================
# FOOTER
# =========================================================
st.divider()
st.markdown(
    "<center><small>📐 MathLearn | Belajar Transformasi Geometri "
    "dengan Interaktif</small></center>",
    unsafe_allow_html=True
)