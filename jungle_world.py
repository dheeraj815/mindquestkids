import streamlit as st


def main():
    st.header("🌴 Jungle World")

    # Pro status
    if "is_pro" not in st.session_state:
        st.session_state.is_pro = False

    # Toggle pro (for demo purposes)
    col1, col2 = st.columns([3, 1])
    with col2:
        if st.session_state.is_pro:
            st.success("👑 PRO User")
            if st.button("Logout Pro"):
                st.session_state.is_pro = False
                st.rerun()
        else:
            if st.button("🔓 Unlock Pro"):
                st.session_state.is_pro = True
                st.rerun()

    questions = [
        # FREE QUESTIONS (1-20)
        {"q": "Which animal is known as the King of the Jungle?", "a": "Lion", "hint": "Roars loudly",
            "exp": "Lions are called King of the Jungle due to their strength and dominance.", "free": True},
        {"q": "Which animal swings from trees using its arms?", "a": "Monkey", "hint": "Loves bananas",
            "exp": "Monkeys use their arms to swing between trees.", "free": True},
        {"q": "Which animal has black and white stripes?", "a": "Zebra", "hint": "Looks like a horse",
            "exp": "Zebras have unique black and white stripes.", "free": True},
        {"q": "Which animal is the largest land mammal?", "a": "Elephant",
            "hint": "Has a trunk", "exp": "Elephants are the largest land mammals.", "free": True},
        {"q": "Which animal is slow and carries a shell?", "a": "Tortoise", "hint": "Lives long",
            "exp": "Tortoises are slow-moving and have hard shells.", "free": True},
        {"q": "Which animal is known for its trunk?", "a": "Elephant", "hint": "Big ears",
            "exp": "Elephants use their trunk to eat, drink, and interact.", "free": True},
        {"q": "Which bird is known for its colorful feathers?", "a": "Peacock",
            "hint": "Famous tail display", "exp": "Peacocks have beautiful, colorful feathers.", "free": True},
        {"q": "Which animal has a long neck?", "a": "Giraffe", "hint": "Eats leaves from tall trees",
            "exp": "Giraffes have long necks to reach high foliage.", "free": True},
        {"q": "Which animal is famous for building dams?", "a": "Beaver",
            "hint": "Lives near water", "exp": "Beavers build dams using wood and mud.", "free": True},
        {"q": "Which animal has a pouch to carry its baby?", "a": "Kangaroo", "hint": "Jumps",
            "exp": "Kangaroos have pouches to carry their joeys.", "free": True},
        {"q": "Which animal sleeps hanging upside down?", "a": "Bat", "hint": "Night flyer",
            "exp": "Bats hang upside down when resting.", "free": True},
        {"q": "Which animal has a prehensile tail?", "a": "Monkey", "hint": "Grips things",
            "exp": "Some monkeys use tails to grab branches.", "free": True},
        {"q": "Which animal is covered with quills?", "a": "Porcupine", "hint": "Sharp defense",
            "exp": "Porcupines use quills to protect themselves.", "free": True},
        {"q": "Which animal rolls into a ball when threatened?", "a": "Hedgehog",
            "hint": "Spiky ball", "exp": "Hedgehogs curl up to protect themselves.", "free": True},
        {"q": "Which animal changes color to hide?", "a": "Chameleon", "hint": "Camouflage expert",
            "exp": "Chameleons change colors for camouflage.", "free": True},
        {"q": "Which animal is known as the Snake of the Jungle?", "a": "Python",
            "hint": "Constrictor", "exp": "Pythons are large constrictor snakes.", "free": True},
        {"q": "Which animal has a long sticky tongue to catch insects?", "a": "Anteater",
            "hint": "Eats ants", "exp": "Anteaters use their tongue to eat ants and termites.", "free": True},
        {"q": "Which animal swings using a long tail?", "a": "Spider Monkey", "hint": "Agile climber",
            "exp": "Spider monkeys use their tail as a fifth limb.", "free": True},
        {"q": "Which animal is nocturnal and hoots?", "a": "Owl", "hint": "Bird of prey",
            "exp": "Owls are active at night and hoot to communicate.", "free": True},
        {"q": "Which animal has a horn on its nose?", "a": "Rhinoceros", "hint": "Thick skin",
            "exp": "Rhinoceroses have one or two horns on their nose.", "free": True},

        # PRO QUESTIONS (21-50)
        {"q": "Which animal has a mane?", "a": "Lion", "hint": "Male only",
            "exp": "Male lions have a mane around their head and neck.", "free": False},
        {"q": "Which animal is known for leaping from trees?", "a": "Leopard", "hint": "Spotted",
            "exp": "Leopards leap to catch prey or move through trees.", "free": False},
        {"q": "Which animal carries its baby in a pouch?", "a": "Kangaroo", "hint": "Marsupial",
            "exp": "Kangaroo mothers carry their young in pouches.", "free": False},
        {"q": "Which animal has wings but cannot fly?", "a": "Penguin", "hint": "Swims well",
            "exp": "Penguins use their wings to swim, not fly.", "free": False},
        {"q": "Which animal hangs by its feet and sleeps upside down?", "a": "Bat",
            "hint": "Uses echolocation", "exp": "Bats hang upside down when resting.", "free": False},
        {"q": "Which animal is known as a skilled climber?", "a": "Monkey", "hint": "Lives in trees",
            "exp": "Monkeys climb trees efficiently using hands and feet.", "free": False},
        {"q": "Which animal has black and white stripes and runs fast?", "a": "Zebra",
            "hint": "Looks like a horse", "exp": "Zebras run quickly to escape predators.", "free": False},
        {"q": "Which animal uses camouflage to hide from predators?", "a": "Chameleon",
            "hint": "Color changes", "exp": "Chameleons change color to blend into surroundings.", "free": False},
        {"q": "Which animal is the largest cat in the jungle?", "a": "Tiger", "hint": "Striped",
            "exp": "Tigers are the largest big cats and have stripes.", "free": False},
        {"q": "Which animal is known for swinging and eating bananas?", "a": "Monkey", "hint": "Tree dweller",
            "exp": "Monkeys swing through trees and eat fruits like bananas.", "free": False},
        {"q": "Which animal has sharp teeth and hunts in packs?", "a": "Wolf", "hint": "Not in jungle but forests",
            "exp": "Wolves hunt in packs using sharp teeth and cooperation.", "free": False},
        {"q": "Which animal is known for its trunk and large ears?", "a": "Elephant", "hint": "Gentle giant",
            "exp": "Elephants use their trunk to grab food and ears to cool down.", "free": False},
        {"q": "Which animal can glide from tree to tree?", "a": "Flying Squirrel",
            "hint": "No wings", "exp": "Flying squirrels glide using a skin membrane.", "free": False},
        {"q": "Which animal builds nests in tall trees?", "a": "Bird", "hint": "Sings in mornings",
            "exp": "Many birds build nests high in trees for safety.", "free": False},
        {"q": "Which animal has venom and a long tongue?", "a": "Komodo Dragon", "hint": "Large lizard",
            "exp": "Komodo dragons have venomous bites and long tongues.", "free": False},
        {"q": "Which animal is a nocturnal predator?", "a": "Owl", "hint": "Hoots at night",
            "exp": "Owls hunt at night using keen eyesight and hearing.", "free": False},
        {"q": "Which animal has spikes for protection?", "a": "Porcupine", "hint": "Quills",
            "exp": "Porcupines use sharp quills to protect themselves.", "free": False},
        {"q": "Which animal is famous for jumping?", "a": "Frog", "hint": "Green and small",
            "exp": "Frogs jump to escape predators and move quickly.", "free": False},
        {"q": "Which animal has the loudest roar?", "a": "Lion", "hint": "King of beasts",
            "exp": "Lions have one of the loudest roars in the animal kingdom.", "free": False},
        {"q": "Which primate is closest to humans?", "a": "Chimpanzee", "hint": "Very intelligent",
            "exp": "Chimpanzees share about 98% of human DNA.", "free": False},
        {"q": "Which animal is the fastest runner in the jungle?", "a": "Jaguar",
            "hint": "Big cat", "exp": "Jaguars are powerful and fast runners.", "free": False},
        {"q": "Which bird cannot fly but runs fast?", "a": "Cassowary", "hint": "Dangerous bird",
            "exp": "Cassowaries are flightless but can run up to 50 km/h.", "free": False},
        {"q": "Which animal uses tools to get food?", "a": "Chimpanzee", "hint": "Smart primate",
            "exp": "Chimpanzees use sticks and stones as tools.", "free": False},
        {"q": "Which snake is the longest?", "a": "Reticulated Python", "hint": "Can grow over 20 feet",
            "exp": "Reticulated pythons are the world's longest snakes.", "free": False},
        {"q": "Which animal has the strongest bite?", "a": "Jaguar", "hint": "Big cat",
            "exp": "Jaguars have the strongest bite force of big cats.", "free": False},
        {"q": "Which bird has the largest wingspan?", "a": "Wandering Albatross", "hint": "Ocean bird",
            "exp": "Wandering albatrosses have wingspans up to 11 feet.", "free": False},
        {"q": "Which animal sleeps the most?", "a": "Sloth", "hint": "Very slow",
            "exp": "Sloths sleep up to 20 hours a day.", "free": False},
        {"q": "Which amphibian is poisonous?", "a": "Poison Dart Frog", "hint": "Brightly colored",
            "exp": "Poison dart frogs have toxic skin secretions.", "free": False},
        {"q": "Which animal has the best night vision?", "a": "Owl", "hint": "Nocturnal hunter",
            "exp": "Owls have exceptional night vision for hunting.", "free": False},
        {"q": "Which mammal can fly?", "a": "Bat", "hint": "Only flying mammal",
            "exp": "Bats are the only mammals capable of true flight.", "free": False}
    ]

    if "answers" not in st.session_state:
        st.session_state.answers = {}
    if "scores" not in st.session_state:
        st.session_state.scores = {}

    for i, q in enumerate(questions):
        # Check if question is locked
        is_locked = not q["free"] and not st.session_state.is_pro

        if is_locked:
            st.subheader(f"Q{i+1}. 🔒 Pro Question")
            st.warning("⭐ Upgrade to Pro to unlock this question!")
        else:
            st.subheader(f"Q{i+1}. {q['q']}")
            st.caption(f"💡 Hint: {q['hint']}")
            st.session_state.answers[i] = st.text_input(
                "Your answer",
                key=f"jungle_world_{i}",
                disabled=is_locked
            )

    if st.button("✅ Submit"):
        score = 0
        available_questions = [i for i, q in enumerate(
            questions) if q["free"] or st.session_state.is_pro]

        for i in available_questions:
            q = questions[i]
            if st.session_state.answers.get(i, "").strip().lower() == q["a"].lower():
                score += 1

        total_available = len(available_questions)
        st.session_state.scores["Jungle World"] = f"{score}/{total_available}"
        st.success(f"Score: {score}/{total_available}")

        for i in available_questions:
            q = questions[i]
            user_answer = st.session_state.answers.get(i, "").strip()
            is_correct = user_answer.lower() == q["a"].lower()

            if is_correct:
                st.success(f"Q{i+1} ✓ Correct! {q['exp']}")
            else:
                st.error(
                    f"Q{i+1} ✗ Wrong! Correct answer: {q['a']}. {q['exp']}")

    if st.button("🔄 Restart"):
        st.session_state.answers = {}
        st.rerun()

    # Show stats
    st.divider()
    if st.session_state.is_pro:
        st.info("📊 You have access to all 50 questions!")
    else:
        st.info(
            "📊 Free: 20/50 questions available. Upgrade to Pro for 30 more questions!")


if __name__ == "__main__":
    main()
