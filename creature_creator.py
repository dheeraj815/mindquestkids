import streamlit as st


def main():
    st.header("🦄 Creature Creator")

    questions = [
        {"q": "Which animal can fly?", "a": "Bird", "hint": "Has wings",
            "exp": "Birds have wings and can fly."},
        {"q": "Which animal lives in water?", "a": "Fish", "hint": "Gills",
            "exp": "Fish live in water and breathe through gills."},
        {"q": "Which animal has a shell?", "a": "Turtle", "hint": "Slow mover",
            "exp": "Turtles have a hard shell for protection."},
        {"q": "Which creature has eight legs?", "a": "Spider",
            "hint": "Creepy crawler", "exp": "Spiders have eight legs."},
        {"q": "Which animal is known for its trunk?", "a": "Elephant",
            "hint": "Big ears", "exp": "Elephants have a trunk and large ears."},
        {"q": "Which animal can change colors?", "a": "Chameleon", "hint": "Camouflage",
            "exp": "Chameleons change color to blend with surroundings."},
        {"q": "Which creature spins webs?", "a": "Spider",
            "hint": "Eight legs", "exp": "Spiders spin webs to catch prey."},
        {"q": "Which animal hops?", "a": "Frog",
            "hint": "Croaks", "exp": "Frogs hop and croak."},
        {"q": "Which animal has stripes?", "a": "Zebra", "hint": "Black and white",
            "exp": "Zebras have black and white stripes."},
        {"q": "Which creature has wings but is not a bird?", "a": "Butterfly",
            "hint": "Colorful wings", "exp": "Butterflies have wings and can fly but are insects."},
        {"q": "Which animal has a long neck?", "a": "Giraffe", "hint": "Tallest land animal",
            "exp": "Giraffes have long necks to reach tree leaves."},
        {"q": "Which creature is known for its shell and slow movement?", "a": "Turtle",
            "hint": "Lives on land and water", "exp": "Turtles are slow-moving reptiles with a protective shell."},
        {"q": "Which animal makes honey?", "a": "Bee",
            "hint": "Buzzes", "exp": "Bees produce honey."},
        {"q": "Which creature has a stinger?", "a": "Bee",
            "hint": "Buzzes", "exp": "Bees have stingers for protection."},
        {"q": "Which animal can swim?", "a": "Dolphin",
            "hint": "Smart marine mammal", "exp": "Dolphins are intelligent swimmers."},
        {"q": "Which animal has tusks?", "a": "Elephant",
            "hint": "Big ears", "exp": "Elephants have tusks and a trunk."},
        {"q": "Which animal is nocturnal?", "a": "Owl",
            "hint": "Hoots at night", "exp": "Owls are active during the night."},
        {"q": "Which creature crawls and has a hard shell?", "a": "Crab",
            "hint": "Beach dweller", "exp": "Crabs crawl sideways and have a hard shell."},
        {"q": "Which animal can mimic human speech?", "a": "Parrot",
            "hint": "Colorful feathers", "exp": "Parrots can mimic human sounds."},
        {"q": "Which animal has a pouch?", "a": "Kangaroo", "hint": "Jumps",
            "exp": "Kangaroos carry their babies in a pouch."},
        {"q": "Which creature has tentacles?", "a": "Octopus",
            "hint": "Lives in water", "exp": "Octopuses have eight tentacles."},
        {"q": "Which animal has a mane?", "a": "Lion",
            "hint": "King of jungle", "exp": "Male lions have a mane."},
        {"q": "Which creature produces silk?", "a": "Silkworm",
            "hint": "Small insect", "exp": "Silkworms produce silk for cocoon."},
        {"q": "Which animal can jump long distances?", "a": "Frog",
            "hint": "Amphibian", "exp": "Frogs can leap long distances."},
        {"q": "Which creature glows in the dark?", "a": "Firefly",
            "hint": "Night insect", "exp": "Fireflies glow using bioluminescence."},
        {"q": "Which animal carries its home on its back?", "a": "Snail",
            "hint": "Sluggish", "exp": "Snails have a shell on their back."},
        {"q": "Which animal lays eggs?", "a": "Chicken",
            "hint": "Farm bird", "exp": "Chickens lay eggs."},
        {"q": "Which creature has scales?", "a": "Fish", "hint": "Lives in water",
            "exp": "Fish have scales covering their body."},
        {"q": "Which animal is known for building dams?", "a": "Beaver",
            "hint": "Lives near water", "exp": "Beavers build dams to create ponds."},
        {"q": "Which animal can walk on two legs?", "a": "Human",
            "hint": "Biped", "exp": "Humans are bipedal and walk on two legs."},
        {"q": "Which animal has sharp claws?", "a": "Tiger",
            "hint": "Big cat", "exp": "Tigers have sharp claws for hunting."},
        {"q": "Which creature spins silk for shelter?", "a": "Spider", "hint": "Web maker",
            "exp": "Spiders spin silk to make webs for shelter and catching prey."},
        {"q": "Which animal hops and carries a baby in a pouch?", "a": "Kangaroo", "hint": "Australian animal",
            "exp": "Kangaroos are marsupials that hop and carry babies in pouches."},
        {"q": "Which animal has antlers?", "a": "Deer",
            "hint": "Forest animal", "exp": "Male deer have antlers."},
        {"q": "Which creature has wings and stings?", "a": "Bee",
            "hint": "Buzzing insect", "exp": "Bees have wings and stingers."},
        {"q": "Which animal sleeps standing up?", "a": "Horse",
            "hint": "Farm animal", "exp": "Horses often sleep while standing."},
        {"q": "Which creature has a long tongue and eats insects?", "a": "Chameleon",
            "hint": "Color-changing", "exp": "Chameleons use long tongues to catch insects."},
        {"q": "Which animal is known for carrying water in its hump?", "a": "Camel",
            "hint": "Desert animal", "exp": "Camels store fat in their humps and survive long without water."},
        {"q": "Which creature has sharp teeth and swims in the ocean?", "a": "Shark",
            "hint": "Dangerous predator", "exp": "Sharks have sharp teeth and are ocean predators."},
        {"q": "Which animal rolls into a ball for protection?", "a": "Hedgehog",
            "hint": "Spiky", "exp": "Hedgehogs curl up to protect themselves from predators."},
        {"q": "Which animal has a long nose and big ears?", "a": "Elephant", "hint": "Largest land animal",
            "exp": "Elephants have a trunk and large ears for hearing and cooling."}
    ]

    if "answers" not in st.session_state:
        st.session_state.answers = {}
    if "scores" not in st.session_state:
        st.session_state.scores = {}

    for i, q in enumerate(questions):
        st.subheader(f"Q{i+1}. {q['q']}")
        st.caption(f"Hint: {q['hint']}")
        st.session_state.answers[i] = st.text_input(
            "Your answer", key=f"creature_creator_{i}")

    if st.button("✅ Submit"):
        score = 0
        for i, q in enumerate(questions):
            if st.session_state.answers.get(i, "").strip().lower() == q["a"].lower():
                score += 1
        st.session_state.scores["Creature Creator"] = f"{score}/{len(questions)}"
        st.success(f"Score: {score}/{len(questions)}")
        for i, q in enumerate(questions):
            st.info(f"Q{i+1} Explanation: {q['exp']}")

    if st.button("🔄 Restart"):
        st.session_state.answers = {}
        st.rerun()
