import streamlit as st
import pandas as pd


def main():
    st.markdown("""
    <style>
        .dashboard-card {
            background: linear-gradient(135deg, #ffffff 0%, #f8f9ff 100%);
            padding: 35px;
            border-radius: 20px;
            box-shadow: 0 10px 40px rgba(31, 38, 135, 0.15);
            margin: 25px 0;
            border-left: 6px solid #667eea;
            transition: all 0.3s ease;
        }
        
        .dashboard-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 15px 50px rgba(31, 38, 135, 0.25);
        }
        
        .stat-box {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 30px;
            border-radius: 15px;
            text-align: center;
            box-shadow: 0 8px 25px rgba(102, 126, 234, 0.4);
            margin: 10px 0;
            transition: all 0.3s ease;
        }
        
        .stat-box:hover {
            transform: translateY(-5px) scale(1.03);
            box-shadow: 0 12px 35px rgba(102, 126, 234, 0.6);
        }
        
        .stat-number {
            font-size: 52px;
            font-weight: 900;
            margin: 10px 0;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.2);
        }
        
        .stat-label {
            font-size: 17px;
            font-weight: 700;
            opacity: 0.95;
            text-transform: uppercase;
            letter-spacing: 1px;
        }
        
        .progress-table {
            background: white;
            border-radius: 15px;
            overflow: hidden;
            box-shadow: 0 8px 25px rgba(0, 0, 0, 0.08);
        }
        
        .completed {
            color: #4CAF50;
            font-weight: 800;
        }
        
        .not-completed {
            color: #ff6b6b;
            font-weight: 700;
        }
        
        .parent-header {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 40px;
            border-radius: 20px;
            text-align: center;
            margin-bottom: 30px;
            box-shadow: 0 10px 40px rgba(102, 126, 234, 0.4);
        }
    </style>
    """, unsafe_allow_html=True)

    child_name = st.session_state.child_name if st.session_state.child_name else "Child"

    st.markdown(f"""
    <div class="parent-header">
        <h1 style="margin: 0; font-size: 48px; font-weight: 900;">👨‍👩‍👧 Parent Dashboard</h1>
        <p style="font-size: 22px; margin-top: 15px; opacity: 0.95;">Monitoring progress for: <strong>{child_name}</strong></p>
    </div>
    """, unsafe_allow_html=True)

    # List of only 5 quizzes
    all_quizzes = [
        "Animal Sound Explorer",
        "Daily Quiz",
        "Creative Drawing",
        "Healthy Eating",
        "Jungle World"
    ]

    # Calculate statistics
    scores_dict = st.session_state.scores
    completed_count = sum(
        1 for quiz in all_quizzes if quiz in scores_dict and scores_dict[quiz] != "❌ Not Completed")
    total_count = len(all_quizzes)
    completion_percentage = int((completed_count / total_count) * 100)

    # Calculate total questions answered and average score
    total_questions_answered = 0
    total_correct = 0

    for quiz in all_quizzes:
        if quiz in scores_dict and scores_dict[quiz] != "❌ Not Completed":
            score_str = scores_dict[quiz]
            if "/" in score_str:
                try:
                    correct, total = score_str.split("/")
                    total_correct += int(correct)
                    total_questions_answered += int(total)
                except:
                    pass

    average_score = int((total_correct / total_questions_answered * 100)
                        ) if total_questions_answered > 0 else 0

    # Display statistics
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown(f"""
        <div class="stat-box">
            <div class="stat-label">Total Quizzes</div>
            <div class="stat-number">{total_count}</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div class="stat-box" style="background: linear-gradient(135deg, #4CAF50 0%, #45a049 100%);">
            <div class="stat-label">Completed</div>
            <div class="stat-number">{completed_count}</div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown(f"""
        <div class="stat-box" style="background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);">
            <div class="stat-label">Progress</div>
            <div class="stat-number">{completion_percentage}%</div>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown(f"""
        <div class="stat-box" style="background: linear-gradient(135deg, #FFD700 0%, #FFA500 100%);">
            <div class="stat-label">Avg Score</div>
            <div class="stat-number" style="color: #000;">{average_score}%</div>
        </div>
        """, unsafe_allow_html=True)

    # Progress bar with custom styling
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
    <div style="background: #f0f0f0; border-radius: 10px; padding: 5px; margin: 20px 0;">
    """, unsafe_allow_html=True)
    st.progress(completion_percentage / 100)
    st.markdown("</div>", unsafe_allow_html=True)

    # Prepare data for table
    data = []
    quiz_emojis = {
        "Animal Sound Explorer": "🐾",
        "Daily Quiz": "📝",
        "Creative Drawing": "🎨",
        "Healthy Eating": "🥗",
        "Jungle World": "🌴"
    }

    for i, quiz in enumerate(all_quizzes, 1):
        score = scores_dict.get(quiz, "❌ Not Completed")
        status = "✅ Completed" if score != "❌ Not Completed" else "⏳ Pending"
        emoji = quiz_emojis.get(quiz, "📚")

        # Calculate percentage if completed
        percentage = ""
        if score != "❌ Not Completed" and "/" in score:
            try:
                correct, total = score.split("/")
                pct = int((int(correct) / int(total)) * 100)
                percentage = f"{pct}%"
            except:
                percentage = "-"
        else:
            percentage = "-"

        data.append({
            "#": i,
            "Quiz": f"{emoji} {quiz}",
            "Score": score,
            "Percentage": percentage,
            "Status": status
        })

    df = pd.DataFrame(data)

    # Display detailed progress
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
    <div class="dashboard-card">
        <h2 style="color: #667eea; margin-bottom: 20px; font-weight: 900;">📊 Detailed Progress Report</h2>
    </div>
    """, unsafe_allow_html=True)

    # Custom table styling
    st.markdown("""
    <style>
        .dataframe {
            font-size: 17px;
            border-radius: 15px;
            overflow: hidden;
        }
        .dataframe thead tr th {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 18px;
            font-weight: 800;
            text-align: left;
            font-size: 16px;
            text-transform: uppercase;
            letter-spacing: 1px;
        }
        .dataframe tbody tr td {
            padding: 15px;
            border-bottom: 2px solid #f0f0f0;
            font-weight: 600;
        }
        .dataframe tbody tr:hover {
            background: linear-gradient(135deg, #f8f9ff 0%, #ffffff 100%);
            transform: scale(1.01);
        }
        .dataframe tbody tr {
            transition: all 0.3s ease;
        }
    </style>
    """, unsafe_allow_html=True)

    st.dataframe(df, use_container_width=True, hide_index=True)

    # Performance analysis
    if completed_count > 0:
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("""
        <div class="dashboard-card" style="border-left: 6px solid #4CAF50;">
            <h3 style="color: #4CAF50; margin-bottom: 15px; font-weight: 900;">📈 Performance Analysis</h3>
        """, unsafe_allow_html=True)

        col1, col2 = st.columns(2)

        with col1:
            st.metric("Total Questions Attempted",
                      total_questions_answered, delta=None)
            st.metric("Questions Answered Correctly",
                      total_correct, delta=None)

        with col2:
            st.metric("Overall Accuracy", f"{average_score}%", delta=None)
            st.metric("Quizzes Remaining", total_count -
                      completed_count, delta=None)

        st.markdown("</div>", unsafe_allow_html=True)

    # Message if no quizzes completed
    if completed_count == 0:
        st.info(
            "🎯 No quiz scores yet. Start exploring the quizzes to see progress here!")
    else:
        st.success(
            f"🎉 Great job! {child_name} has completed {completed_count} out of {total_count} quizzes!")

        # Show encouragement based on average score
        if average_score >= 80:
            st.balloons()
            st.markdown("""
            <div class="dashboard-card" style="background: linear-gradient(135deg, #4CAF50 0%, #45a049 100%); color: white; border: none;">
                <h3 style="color: white;">🌟 Outstanding Performance!</h3>
                <p style="font-size: 18px; opacity: 0.95;">{child_name} is doing exceptionally well! Keep up the amazing work!</p>
            </div>
            """.format(child_name=child_name), unsafe_allow_html=True)
        elif average_score >= 60:
            st.markdown("""
            <div class="dashboard-card" style="background: linear-gradient(135deg, #2196F3 0%, #1976D2 100%); color: white; border: none;">
                <h3 style="color: white;">👍 Good Progress!</h3>
                <p style="font-size: 18px; opacity: 0.95;">{child_name} is learning well! A little more practice will lead to excellence!</p>
            </div>
            """.format(child_name=child_name), unsafe_allow_html=True)
        else:
            st.markdown("""
            <div class="dashboard-card" style="background: linear-gradient(135deg, #FF9800 0%, #F57C00 100%); color: white; border: none;">
                <h3 style="color: white;">💪 Keep Learning!</h3>
                <p style="font-size: 18px; opacity: 0.95;">Every expert was once a beginner. Encourage {child_name} to keep practicing!</p>
            </div>
            """.format(child_name=child_name), unsafe_allow_html=True)

    # Action buttons
    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 1, 2])

    with col1:
        if st.button("🔄 Reset All Scores", use_container_width=True):
            st.session_state.scores = {}
            st.success("All scores have been reset!")
            st.rerun()

    with col2:
        if st.button("📥 Export Report", use_container_width=True):
            csv = df.to_csv(index=False)
            st.download_button(
                label="⬇️ Download CSV",
                data=csv,
                file_name=f"{child_name}_progress_report.csv",
                mime="text/csv",
                use_container_width=True
            )

    # Tips for parents
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
    <div class="dashboard-card" style="border-left: 6px solid #FFD700;">
        <h3 style="color: #FFA500; margin-bottom: 20px; font-weight: 900;">💡 Tips for Parents</h3>
        <ul style="line-height: 2.2; font-size: 17px; color: #333;">
            <li>🎯 <strong>Encourage at their pace</strong> - Let your child complete quizzes without pressure</li>
            <li>🎉 <strong>Celebrate achievements</strong> - Every small win builds confidence</li>
            <li>📚 <strong>Review together</strong> - Turn mistakes into learning opportunities</li>
            <li>⏰ <strong>Set routine</strong> - Regular practice leads to better retention</li>
            <li>💪 <strong>Growth mindset</strong> - Praise effort and persistence, not just results</li>
            <li>🌟 <strong>Make it fun</strong> - Learning should be enjoyable, not stressful</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    # Pro membership info
    if not st.session_state.is_pro:
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("""
        <div class="dashboard-card" style="background: linear-gradient(135deg, #FFD700 0%, #FFA500 100%); border: none;">
            <h3 style="color: #000; margin-bottom: 15px; font-weight: 900;">👑 Upgrade to PRO for More Insights!</h3>
            <p style="font-size: 17px; color: #000; line-height: 1.8;">
                ✨ Get access to all 50 questions per quiz (250+ total)<br>
                📊 Detailed performance analytics and trends<br>
                🏆 Printable certificates of achievement<br>
                💾 Export detailed progress reports
            </p>
        </div>
        """, unsafe_allow_html=True)


if __name__ == "__main__":
    main()
