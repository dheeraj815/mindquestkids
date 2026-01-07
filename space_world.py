import streamlit as st


def main():
    st.header("🚀 Space World")

    questions = [
        {"q": "What is the center of our Solar System?", "a": "Sun", "hint": "It gives us light",
            "exp": "The Sun is the star at the center of our Solar System."},
        {"q": "Which planet is known as the Red Planet?", "a": "Mars", "hint": "Looks red in the sky",
            "exp": "Mars is called the Red Planet due to its reddish surface."},
        {"q": "Which planet is the largest in our Solar System?", "a": "Jupiter", "hint": "Has a big red spot",
            "exp": "Jupiter is the largest planet with a giant storm called the Great Red Spot."},
        {"q": "Which planet is closest to the Sun?", "a": "Mercury",
            "hint": "Small and fast", "exp": "Mercury is the closest planet to the Sun."},
        {"q": "Which planet is famous for its rings?", "a": "Saturn",
            "hint": "Has beautiful rings", "exp": "Saturn has prominent rings made of ice and rock."},
        {"q": "Which planet is known as the Blue Planet?", "a": "Earth", "hint": "We live here",
            "exp": "Earth is called the Blue Planet because of its oceans."},
        {"q": "Which planet has a tilted axis causing seasons?", "a": "Earth",
            "hint": "Day & night length change", "exp": "Earth's tilted axis gives us seasons."},
        {"q": "Which planet is known for extreme winds and storms?", "a": "Neptune",
            "hint": "Farthest planet", "exp": "Neptune has strong winds and storms."},
        {"q": "Which planet is known as the Morning Star?", "a": "Venus", "hint": "Bright and beautiful",
            "exp": "Venus is called the Morning Star because it shines brightly in the sky."},
        {"q": "Which planet has a day longer than its year?", "a": "Venus", "hint": "Spins slowly",
            "exp": "Venus rotates slowly, making its day longer than its orbit around the Sun."},
        {"q": "Which planet is famous for its Great Red Spot?", "a": "Jupiter",
            "hint": "Storm", "exp": "Jupiter's Great Red Spot is a huge storm."},
        {"q": "Which planet is known as the Ice Giant?", "a": "Uranus", "hint": "Cold and blue-green",
            "exp": "Uranus is called an Ice Giant due to its cold atmosphere."},
        {"q": "Which planet spins on its side?", "a": "Uranus", "hint": "Unusual tilt",
            "exp": "Uranus rotates almost horizontally on its side."},
        {"q": "Which planet has the most moons?", "a": "Saturn", "hint": "Many orbiting objects",
            "exp": "Saturn has the largest number of known moons."},
        {"q": "Which planet is known for its strong winds and blue color?", "a": "Neptune",
            "hint": "Farthest planet", "exp": "Neptune appears blue due to methane and has strong winds."},
        {"q": "Which celestial body orbits planets?", "a": "Moon",
            "hint": "Earth has one", "exp": "Moons orbit planets."},
        {"q": "Which planet is called the Earth's twin?", "a": "Venus",
            "hint": "Similar size", "exp": "Venus is similar in size to Earth."},
        {"q": "Which planet is known as the Gas Giant?", "a": "Jupiter", "hint": "Biggest planet",
            "exp": "Jupiter is a Gas Giant made mostly of hydrogen and helium."},
        {"q": "Which planet has a surface with volcanoes and craters?", "a": "Mars",
            "hint": "Red surface", "exp": "Mars has volcanoes like Olympus Mons and many craters."},
        {"q": "Which planet is known for its bright white clouds?", "a": "Venus",
            "hint": "Hot and cloudy", "exp": "Venus has thick, bright white clouds of sulfuric acid."},
        {"q": "Which planet has a ring system besides Saturn?", "a": "Jupiter",
            "hint": "Faint rings", "exp": "Jupiter has faint rings made of dust."},
        {"q": "Which planet is known for extreme cold?", "a": "Neptune", "hint": "Blue and far",
            "exp": "Neptune is extremely cold because it is far from the Sun."},
        {"q": "Which planet has a surface mostly made of rock?", "a": "Earth",
            "hint": "We live on it", "exp": "Earth's surface is mostly rocky land and water."},
        {"q": "Which planet is known as the Morning and Evening Star?", "a": "Venus",
            "hint": "Bright appearance", "exp": "Venus is visible in the sky both morning and evening."},
        {"q": "Which planet rotates fastest?", "a": "Jupiter", "hint": "Short day",
            "exp": "Jupiter rotates once every 10 hours, the fastest in the Solar System."},
        {"q": "Which planet has the tallest volcano?", "a": "Mars", "hint": "Olympus Mons",
            "exp": "Mars has Olympus Mons, the tallest volcano in the Solar System."},
        {"q": "Which planet has a very thin atmosphere?", "a": "Mercury",
            "hint": "No weather", "exp": "Mercury has almost no atmosphere."},
        {"q": "Which planet has strong magnetic field?", "a": "Jupiter", "hint": "Protects from solar wind",
            "exp": "Jupiter's magnetic field is the strongest among planets."},
        {"q": "Which planet is known for its tilted axis and rings?", "a": "Uranus",
            "hint": "Sideways rotation", "exp": "Uranus has rings and spins on its side."},
        {"q": "Which planet is the hottest in the Solar System?", "a": "Venus",
            "hint": "Greenhouse effect", "exp": "Venus is hottest due to dense atmosphere trapping heat."},
        {"q": "Which planet has frozen water at its poles?", "a": "Mars",
            "hint": "Red planet ice", "exp": "Mars has ice caps at its poles."},
        {"q": "Which planet is smallest in the Solar System?", "a": "Mercury",
            "hint": "Closest to Sun", "exp": "Mercury is the smallest planet."},
        {"q": "Which planet appears reddish due to iron oxide?", "a": "Mars", "hint": "Red soil",
            "exp": "Mars' surface contains iron oxide, giving it a red color."},
        {"q": "Which planet has the most spectacular ring system?", "a": "Saturn",
            "hint": "Visible in telescope", "exp": "Saturn's rings are the most prominent and beautiful."},
        {"q": "Which planet has methane in its atmosphere giving it a blue color?", "a": "Neptune",
            "hint": "Far and cold", "exp": "Methane in Neptune's atmosphere gives it a deep blue color."},
        {"q": "Which planet is known for storms and fast winds?", "a": "Neptune",
            "hint": "Great Dark Spot", "exp": "Neptune has the Great Dark Spot storm and very strong winds."},
        {"q": "Which planet has largest moon called Ganymede?", "a": "Jupiter", "hint": "Bigger than Mercury",
            "exp": "Ganymede is Jupiter's largest moon and the biggest in the Solar System."},
        {"q": "Which planet has the most eccentric orbit?", "a": "Mercury",
            "hint": "Elongated path", "exp": "Mercury's orbit is the most elliptical among planets."}
    ]

    if "answers" not in st.session_state:
        st.session_state.answers = {}
    if "scores" not in st.session_state:
        st.session_state.scores = {}

    for i, q in enumerate(questions):
        st.subheader(f"Q{i+1}. {q['q']}")
        st.caption(f"Hint: {q['hint']}")
        st.session_state.answers[i] = st.text_input(
            "Your answer", key=f"space_world_{i}")

    if st.button("✅ Submit"):
        score = 0
        for i, q in enumerate(questions):
            if st.session_state.answers.get(i, "").strip().lower() == q["a"].lower():
                score += 1
        st.session_state.scores["Space World"] = f"{score}/{len(questions)}"
        st.success(f"Score: {score}/{len(questions)}")
        for i, q in enumerate(questions):
            st.info(f"Q{i+1} Explanation: {q['exp']}")

    if st.button("🔄 Restart"):
        st.session_state.answers = {}
        st.rerun()
