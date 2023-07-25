import anki

# Path to the .apkg file
apkg_file = "Most_Common_3000_Chinese_Hanzi_Characters.apkg"

# Create an Anki Collection object
col = anki.Collection()

# Load the .apkg file into the collection
col.media.importing.importFile(apkg_file)

# Get all decks in the collection
decks = col.decks.allNames()

# Iterate over each deck
for deck_name in decks:
    # Get the deck ID
    deck_id = col.decks.id(deck_name)

    # Get all cards in the deck
    cards = col.db.list("select id from cards where did = ?", deck_id)

    # Iterate over each card
    for card_id in cards:
        # Get the card's question and answer
        card = col.getCard(card_id)
        question = card.note().fields[0]
        answer = card.note().fields[1]

        # Process the question and answer as needed
        # For example, print them to the console
        print("Question:", question)
        print("Answer:", answer)
        print("---")

# Close the collection
col.close()

