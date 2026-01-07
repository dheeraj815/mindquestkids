import streamlit as st
from streamlit_extras.let_it_rain import rain
import time

# ---------------------------------
# PAGE CONFIG
# ---------------------------------
st.set_page_config(
    page_title="MindQuest Kids - Educational Platform",
    page_icon="🌟",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------------------------
# SESSION STATE
# ---------------------------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "child_name" not in st.session_state:
    st.session_state.child_name = ""
if "page" not in st.session_state:
    st.session_state.page = "Home"
if "scores" not in st.session_state:
    st.session_state.scores = {}
if "answers" not in st.session_state:
    st.session_state.answers = {}
if "is_pro" not in st.session_state:
    st.session_state.is_pro = False
if "quiz_attempts" not in st.session_state:
    st.session_state.quiz_attempts = {}

# ---------------------------------
# LOGIN FUNCTIONS
# ---------------------------------


def login(name):
    if name.strip():
        st.session_state.logged_in = True
        st.session_state.child_name = name.strip()
        st.session_state.page = "Home"
        st.rerun()


def logout():
    st.session_state.logged_in = False
    st.session_state.child_name = ""
    st.session_state.page = "Home"
    st.session_state.scores = {}
    st.session_state.answers = {}
    st.rerun()


# ---------------------------------
# ULTRA PROFESSIONAL STYLING
# ---------------------------------
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700;900&display=swap');
    
    * {
        font-family: 'Poppins', sans-serif;
    }
    
    /* Animated Gradient Background */
    .stApp {
        background: linear-gradient(-45deg, #667eea, #764ba2, #f093fb, #4facfe, #00f2fe, #43e97b, #fa709a);
        background-size: 400% 400%;
        animation: gradientFlow 20s ease infinite;
    }
    
    @keyframes gradientFlow {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    /* Glass Morphism Main Container */
    .main .block-container {
        padding: 2.5rem 4rem;
        background: rgba(255, 255, 255, 0.95);
        border-radius: 30px;
        box-shadow: 
            0 8px 32px 0 rgba(31, 38, 135, 0.37),
            0 0 0 1px rgba(255, 255, 255, 0.18);
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        margin: 2.5rem auto;
        max-width: 1500px;
        border: 1px solid rgba(255, 255, 255, 0.3);
    }
    
    /* Stunning Title with Gradient */
    .main-title {
        font-size: 72px;
        font-weight: 900;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        text-align: center;
        margin-bottom: 15px;
        letter-spacing: -2px;
        animation: titleGlow 3s ease-in-out infinite;
        text-shadow: 0 0 30px rgba(102, 126, 234, 0.3);
    }
    
    @keyframes titleGlow {
        0%, 100% { 
            transform: translateY(0px) scale(1);
            filter: brightness(1);
        }
        50% { 
            transform: translateY(-8px) scale(1.02);
            filter: brightness(1.1);
        }
    }
    
    .sub-title {
        font-size: 28px;
        text-align: center;
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 50%, #ffa94d 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-weight: 700;
        margin-bottom: 50px;
        letter-spacing: 3px;
        text-transform: uppercase;
    }
    
    /* Premium 3D Card Design */
    .info-box {
        background: linear-gradient(135deg, #ffffff 0%, #f8f9ff 100%);
        padding: 40px;
        border-radius: 25px;
        box-shadow: 
            0 20px 60px rgba(31, 38, 135, 0.15),
            0 0 0 1px rgba(102, 126, 234, 0.1),
            inset 0 1px 0 rgba(255, 255, 255, 0.9);
        border: 2px solid rgba(102, 126, 234, 0.1);
        font-size: 17px;
        line-height: 2;
        margin: 25px 0;
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        position: relative;
        overflow: hidden;
    }
    
    .info-box::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.4), transparent);
        transition: left 0.5s;
    }
    
    .info-box:hover {
        transform: translateY(-8px) scale(1.02);
        box-shadow: 
            0 30px 80px rgba(31, 38, 135, 0.25),
            0 0 0 1px rgba(102, 126, 234, 0.2);
    }
    
    .info-box:hover::before {
        left: 100%;
    }
    
    /* Animated Pro Badge */
    .pro-badge {
        background: linear-gradient(135deg, #FFD700 0%, #FFA500 50%, #FF6B6B 100%);
        color: #000;
        padding: 10px 25px;
        border-radius: 30px;
        font-weight: 900;
        font-size: 15px;
        display: inline-block;
        box-shadow: 
            0 8px 25px rgba(255, 215, 0, 0.5),
            inset 0 1px 0 rgba(255, 255, 255, 0.6);
        animation: proPulse 2s infinite, proGlow 3s infinite;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    @keyframes proPulse {
        0%, 100% { transform: scale(1); }
        50% { transform: scale(1.08); }
    }
    
    @keyframes proGlow {
        0%, 100% { box-shadow: 0 8px 25px rgba(255, 215, 0, 0.5); }
        50% { box-shadow: 0 8px 35px rgba(255, 215, 0, 0.8); }
    }
    
    /* Premium Sidebar with Gradient */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
        padding: 25px 15px;
        box-shadow: 4px 0 20px rgba(0, 0, 0, 0.1);
    }
    
    [data-testid="stSidebar"] .stMarkdown {
        color: white;
    }
    
    [data-testid="stSidebar"] h3 {
        color: white !important;
        font-weight: 800;
        text-shadow: 2px 2px 8px rgba(0,0,0,0.3);
        font-size: 20px;
        letter-spacing: 1px;
    }
    
    /* Stunning 3D Buttons */
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 20px;
        padding: 16px 32px;
        font-size: 18px;
        font-weight: 800;
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        box-shadow: 
            0 10px 30px rgba(102, 126, 234, 0.4),
            inset 0 1px 0 rgba(255, 255, 255, 0.3);
        text-transform: uppercase;
        letter-spacing: 2px;
        position: relative;
        overflow: hidden;
    }
    
    .stButton > button::before {
        content: '';
        position: absolute;
        top: 50%;
        left: 50%;
        width: 0;
        height: 0;
        border-radius: 50%;
        background: rgba(255, 255, 255, 0.3);
        transform: translate(-50%, -50%);
        transition: width 0.6s, height 0.6s;
    }
    
    .stButton > button:hover::before {
        width: 300px;
        height: 300px;
    }
    
    .stButton > button:hover {
        transform: translateY(-5px) scale(1.05);
        box-shadow: 
            0 15px 40px rgba(102, 126, 234, 0.6),
            inset 0 1px 0 rgba(255, 255, 255, 0.4);
    }
    
    .stButton > button:active {
        transform: translateY(-2px) scale(1.02);
    }
    
    /* Modern Input Fields */
    .stTextInput > div > div > input {
        border-radius: 20px;
        border: 2px solid #e0e0e0;
        padding: 16px 20px;
        font-size: 17px;
        transition: all 0.3s ease;
        background: linear-gradient(135deg, #f8f9ff 0%, #ffffff 100%);
        box-shadow: inset 0 2px 4px rgba(0, 0, 0, 0.05);
    }
    
    .stTextInput > div > div > input:focus {
        border-color: #667eea;
        box-shadow: 
            0 0 0 4px rgba(102, 126, 234, 0.15),
            inset 0 2px 4px rgba(0, 0, 0, 0.05);
        background: white;
        transform: translateY(-2px);
    }
    
    /* Enhanced Footer */
    .footer {
        text-align: center;
        color: #888;
        font-size: 16px;
        padding: 30px;
        margin-top: 60px;
        border-top: 3px solid transparent;
        border-image: linear-gradient(90deg, #667eea, #764ba2, #f093fb);
        border-image-slice: 1;
        font-weight: 600;
    }
    
    /* Beautiful Alert Messages */
    .stSuccess {
        background: linear-gradient(135deg, #4CAF50 0%, #45a049 100%);
        color: white;
        border-radius: 20px;
        padding: 20px;
        font-weight: 700;
        box-shadow: 0 8px 20px rgba(76, 175, 80, 0.4);
        border: none;
    }
    
    .stWarning {
        background: linear-gradient(135deg, #FF9800 0%, #F57C00 100%);
        color: white;
        border-radius: 20px;
        padding: 20px;
        font-weight: 700;
        box-shadow: 0 8px 20px rgba(255, 152, 0, 0.4);
    }
    
    .stInfo {
        background: linear-gradient(135deg, #2196F3 0%, #1976D2 100%);
        color: white;
        border-radius: 20px;
        padding: 20px;
        font-weight: 700;
        box-shadow: 0 8px 20px rgba(33, 150, 243, 0.4);
    }
    
    .stError {
        background: linear-gradient(135deg, #f44336 0%, #d32f2f 100%);
        color: white;
        border-radius: 20px;
        padding: 20px;
        font-weight: 700;
        box-shadow: 0 8px 20px rgba(244, 67, 54, 0.4);
    }
    
    /* Premium Radio Buttons */
    .stRadio > label {
        color: white !important;
        font-weight: 800;
        font-size: 16px;
        text-shadow: 1px 1px 3px rgba(0,0,0,0.2);
    }
    
    .stRadio [role="radiogroup"] label {
        background: rgba(255, 255, 255, 0.2);
        padding: 12px 18px;
        border-radius: 15px;
        margin: 6px 0;
        transition: all 0.3s ease;
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.3);
    }
    
    .stRadio [role="radiogroup"] label:hover {
        background: rgba(255, 255, 255, 0.35);
        transform: translateX(5px);
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
    }
    
    /* Beautiful Headers */
    h1, h2, h3 {
        color: #667eea;
        font-weight: 900;
        letter-spacing: -0.5px;
    }
    
    /* Premium Features Box with Animation */
    .premium-box {
        background: linear-gradient(135deg, #FFD700 0%, #FFA500 50%, #FF6B6B 100%);
        padding: 35px;
        border-radius: 25px;
        color: #000;
        font-weight: 700;
        box-shadow: 
            0 15px 50px rgba(255, 215, 0, 0.4),
            inset 0 2px 0 rgba(255, 255, 255, 0.5);
        margin: 25px 0;
        position: relative;
        overflow: hidden;
        animation: premiumShine 3s infinite;
    }
    
    @keyframes premiumShine {
        0%, 100% { box-shadow: 0 15px 50px rgba(255, 215, 0, 0.4); }
        50% { box-shadow: 0 15px 60px rgba(255, 215, 0, 0.7); }
    }
    
    .premium-box::before {
        content: '✨';
        position: absolute;
        top: 10px;
        right: 10px;
        font-size: 30px;
        animation: sparkle 2s infinite;
    }
    
    @keyframes sparkle {
        0%, 100% { transform: scale(1) rotate(0deg); opacity: 1; }
        50% { transform: scale(1.2) rotate(180deg); opacity: 0.7; }
    }
    
    /* Scrollbar */
    ::-webkit-scrollbar {
        width: 12px;
    }
    
    ::-webkit-scrollbar-track {
        background: #f1f1f1;
        border-radius: 10px;
    }
    
    ::-webkit-scrollbar-thumb {
        background: linear-gradient(180deg, #667eea, #764ba2);
        border-radius: 10px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: linear-gradient(180deg, #764ba2, #667eea);
    }
</style>
""", unsafe_allow_html=True)

# ---------------------------------
# LOGIN SCREEN
# ---------------------------------
if not st.session_state.logged_in:
    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        st.markdown("<div class='main-title'>🌟 MindQuest Kids</div>",
                    unsafe_allow_html=True)
        st.markdown(
            "<div class='sub-title'>LEARN • PLAY • IMAGINE • GROW</div>", unsafe_allow_html=True)
        st.markdown("---")

        st.markdown("### 👦 Welcome to Your Learning Adventure!")
        name = st.text_input(
            "Enter Your Name", placeholder="e.g. Aarav", label_visibility="collapsed")

        if st.button("🚀 START MY ADVENTURE", use_container_width=True):
            if name.strip():
                login(name)
            else:
                st.warning("Please enter your name!")

        st.markdown("""
        <div class="info-box">
            <h3 style="color: #667eea; margin-bottom: 20px;">🎯 What Makes Us Special?</h3>
            <ul style="list-style: none; padding: 0;">
                <li style="padding: 10px 0;">🎨 <strong>250+ Interactive Questions</strong> - Fun & Educational</li>
                <li style="padding: 10px 0;">✨ <strong>5 Quiz Categories</strong> - Animals, Drawing, Health & More</li>
                <li style="padding: 10px 0;">🏆 <strong>Progress Tracking</strong> - See Your Growth</li>
                <li style="padding: 10px 0;">👨‍👩‍👧 <strong>Parent Dashboard</strong> - Monitor Performance</li>
                <li style="padding: 10px 0;">💖 <strong>100% Safe</strong> - No Ads, Kid-Friendly</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="premium-box">
            <h3 style="margin-bottom: 15px;">⭐ FREE + PRO Features</h3>
            <p style="font-size: 16px; line-height: 1.8;">
                🎁 <strong>FREE:</strong> 20 questions per quiz (100+ total)<br>
                👑 <strong>PRO:</strong> All 50 questions per quiz (250+ total) + Special features<br><br>
                <strong>Try FREE first, upgrade anytime!</strong>
            </p>
        </div>
        """, unsafe_allow_html=True)

    st.stop()

# ---------------------------------
# SIDEBAR NAVIGATION
# ---------------------------------
with st.sidebar:
    st.markdown(f"### 👋 Hello, {st.session_state.child_name}!")

    # Show Pro Status
    if st.session_state.is_pro:
        st.markdown('<span class="pro-badge">👑 PRO MEMBER</span>',
                    unsafe_allow_html=True)
    else:
        st.markdown('<span style="background: linear-gradient(135deg, #e0e0e0, #f0f0f0); padding: 8px 18px; border-radius: 25px; font-size: 14px; font-weight: 700; display: inline-block; box-shadow: 0 4px 10px rgba(0,0,0,0.1);">🎁 FREE PLAN</span>', unsafe_allow_html=True)

    st.markdown("---")

    st.markdown("### 📚 Choose Your Adventure")
    st.session_state.page = st.radio(
        "Navigate to:",
        [
            "🏠 Home",
            "👨‍👩‍👧 Parent Dashboard",
            "👑 Upgrade to PRO",
            "───────────",
            "🐾 Animal Sound Explorer",
            "📝 Daily Quiz",
            "🎨 Creative Drawing",
            "🥗 Healthy Eating",
            "🌴 Jungle World",
        ],
        label_visibility="collapsed"
    )

    st.markdown("---")

    # Stats in sidebar
    completed = len(st.session_state.scores)
    st.markdown(f"""
    <div style="background: rgba(255,255,255,0.25); padding: 18px; border-radius: 15px; margin: 12px 0; backdrop-filter: blur(10px); border: 1px solid rgba(255,255,255,0.3);">
        <p style="margin: 8px 0; font-size: 15px; font-weight: 600;">📊 <strong>Quizzes Completed:</strong> {completed}</p>
        <p style="margin: 8px 0; font-size: 15px; font-weight: 600;">🎯 <strong>Account Type:</strong> {'PRO 👑' if st.session_state.is_pro else 'FREE 🎁'}</p>
    </div>
    """, unsafe_allow_html=True)

    if st.button("🚪 LOGOUT", use_container_width=True):
        logout()

# Fun animation
rain(emoji="✨", font_size=20, falling_speed=4, animation_length="infinite")

# ---------------------------------
# MODULE LOADER
# ---------------------------------


def load_module(page):
    try:
        page_clean = page.replace("🐾 ", "").replace("📝 ", "").replace("🎨 ", "").replace(
            "🥗 ", "").replace("🌴 ", "")

        if "Parent Dashboard" in page:
            from quizzes import parent_dashboard as m
        elif "Animal Sound Explorer" in page_clean:
            from quizzes import animal_sound_explorer as m
        elif "Daily Quiz" in page_clean:
            from quizzes import dailyquiz as m
        elif "Healthy Eating" in page_clean:
            from quizzes import healthy_eating as m
        elif "Creative Drawing" in page_clean:
            from quizzes import creative_drawing as m
        elif "Jungle World" in page_clean:
            from quizzes import jungle_world as m
        else:
            return
        m.main()
    except Exception as e:
        st.error("⚠️ Module loading error")
        st.exception(e)


# ---------------------------------
# MAIN CONTENT AREA
# ---------------------------------
if st.session_state.page == "🏠 Home":
    st.markdown("<div class='main-title'>🌟 MindQuest Kids</div>",
                unsafe_allow_html=True)
    st.markdown("<div class='sub-title'>Your Learning Adventure Starts Here!</div>",
                unsafe_allow_html=True)
    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div class="info-box">
            <h3 style="color: #667eea;">🎯 What You'll Learn</h3>
            <ul style="line-height: 2;">
                <li>🧠 Build knowledge through 250+ fun quizzes</li>
                <li>🎨 Improve creativity with art activities</li>
                <li>💪 Develop healthy habits</li>
                <li>🌟 Learn through interactive games</li>
                <li>🏆 Track your progress daily</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="info-box">
            <h3 style="color: #764ba2;">🚀 Getting Started</h3>
            <ul style="line-height: 2;">
                <li>📚 Choose any quiz from sidebar</li>
                <li>📝 Answer 20 FREE questions</li>
                <li>🏆 Check your score instantly</li>
                <li>👑 Upgrade for 30 more questions!</li>
                <li>🎉 Celebrate achievements!</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <div class="info-box" style="text-align: center; margin-top: 30px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white;">
        <h2 style="color: white;">👈 Select any quiz from the sidebar to begin!</h2>
        <p style="font-size: 20px; margin-top: 20px; color: rgba(255,255,255,0.95);">Let's make learning fun and exciting! 🎊</p>
    </div>
    """, unsafe_allow_html=True)

elif st.session_state.page == "👑 Upgrade to PRO":
    st.markdown("## 👑 Upgrade to MindQuest PRO")
    st.markdown("---")

    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown("""
        <div class="premium-box" style="min-height: 400px;">
            <h2 style="margin-bottom: 20px;">🌟 MindQuest PRO Benefits</h2>
            <ul style="font-size: 18px; line-height: 2.5;">
                <li>✅ <strong>Access to ALL 250+ Questions</strong> (30 more per quiz)</li>
                <li>✅ <strong>Detailed Progress Reports</strong></li>
                <li>✅ <strong>Certificate of Achievement</strong></li>
                <li>✅ <strong>Priority Support</strong></li>
                <li>✅ <strong>New Quizzes Every Month</strong></li>
                <li>✅ <strong>Ad-Free Experience Forever</strong></li>
                <li>✅ <strong>Offline Access</strong></li>
            </ul>
            <h3 style="margin-top: 30px; font-size: 32px;">Only ₹299/year or ₹49/month</h3>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="info-box" style="text-align: center; background: white;">
            <h3 style="color: #667eea;">📊 Comparison</h3>
            <table style="width: 100%; margin-top: 20px; font-size: 15px;">
                <tr style="border-bottom: 2px solid #e0e0e0;">
                    <th style="padding: 12px; text-align: left;">Feature</th>
                    <th style="padding: 12px;">FREE</th>
                    <th style="padding: 12px;">PRO</th>
                </tr>
                <tr style="border-bottom: 1px solid #f0f0f0;">
                    <td style="padding: 12px;">Questions</td>
                    <td style="padding: 12px; text-align: center;">100+</td>
                    <td style="padding: 12px; text-align: center; color: #FFD700; font-weight: bold;">250+</td>
                </tr>
                <tr style="border-bottom: 1px solid #f0f0f0;">
                    <td style="padding: 12px;">Progress Tracking</td>
                    <td style="padding: 12px; text-align: center;">✅</td>
                    <td style="padding: 12px; text-align: center;">✅</td>
                </tr>
                <tr style="border-bottom: 1px solid #f0f0f0;">
                    <td style="padding: 12px;">Certificates</td>
                    <td style="padding: 12px; text-align: center;">❌</td>
                    <td style="padding: 12px; text-align: center; color: #FFD700; font-weight: bold;">✅</td>
                </tr>
                <tr>
                    <td style="padding: 12px;">Support</td>
                    <td style="padding: 12px; text-align: center;">Basic</td>
                    <td style="padding: 12px; text-align: center; color: #FFD700; font-weight: bold;">Priority</td>
                </tr>
            </table>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Payment Demo Button
    if not st.session_state.is_pro:
        if st.button("💳 ACTIVATE PRO MEMBERSHIP (Demo)", use_container_width=True):
            with st.spinner("Processing your upgrade..."):
                time.sleep(2)
            st.session_state.is_pro = True
            st.success("🎉 Congratulations! You are now a PRO member!")
            st.balloons()
            time.sleep(1)
            st.rerun()
    else:
        st.success("✅ You are already a PRO member! Enjoy all features! 🎉")

elif st.session_state.page == "───────────":
    st.info("Please select a quiz from the menu above!")

else:
    if "Home" not in st.session_state.page and "Dashboard" not in st.session_state.page and "PRO" not in st.session_state.page and "───" not in st.session_state.page:
        st.markdown(f"## ✨ {st.session_state.page}")
        st.markdown("---")
    load_module(st.session_state.page)

# ---------------------------------
# FOOTER
# ---------------------------------
st.markdown("---")
st.markdown(
    "<div class='footer'>© 2025 MindQuest Kids • Built with ❤️ for Children • Professional Educational Platform</div>",
    unsafe_allow_html=True
)
