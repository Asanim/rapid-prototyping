# Anki Character Categorization

This repository contains code designed to read, categorize, and process character data for later use in AnkiDroid, allowing users to efficiently manage their Anki decks, specifically for Japanese language learning or similar character-based studies. It includes a solution for extracting, modifying, and analyzing data from Anki deck files in the `.apkg` format, typically containing character-based flashcards.

## Setup

1. **Download Anki**  
   To get started, download Anki from [here](https://apps.ankiweb.net/).

2. **Install AnkiConnect**  
   Install the [AnkiConnect](https://ankiweb.net/shared/info/2055492159) add-on to enable communication between Anki and external scripts.

3. **Obtain Shared Decks**  
   Find shared decks on AnkiWeb that contain character data you want to use. For example, you can download Japanese learning decks from [this page](https://ankiweb.net/shared/decks/japanese).

4. **Database Structure**  
   You can explore the structure of Anki decks in detail through the official [Anki-Android Wiki: Database Structure](https://github.com/ankidroid/Anki-Android/wiki/Database-Structure).

   Example structure:
   ```
   ├── example
   │   ├── example.anki2
   │   └── media
   └── example.apkg
   ```

   On Linux, you can use tools like `sqliteman` or `sqlite3` to read and modify `.anki2` files, which contain the database for your Anki decks.

## Example Code for Processing Anki Decks

`text-to-anki.py`: demonstrates how to unzip an `.apkg` file, parse its SQLite database in Anki version 2 format, and perform modifications to the deck.

### Notes Table Structure

The `notes` table stores raw information formatted into flashcards:

```sql
CREATE TABLE notes (
    id              integer primary key,
    guid            text not null,
    mid             integer not null,
    mod             integer not null,
    usn             integer not null,
    tags            text not null,
    flds            text not null,
    sfld            integer not null,
    csum            integer not null,
    flags           integer not null,
    data            text not null
);
```

Example entry:
```
(1453219106197, 'o_4h`pop|W', 1453218888792, 1457014305, 0, '', '人\x1f人\x1f亻&nbsp;\x1f\x1fhuman, person, people\xfrén\x1fNote similarity to 八, which means eight.&nbsp;\x1f今仁休位他\x1f[sound:pronunciation_zh_人.mp3]', '人', 1225946906, 0, '')
```

The data in the `notes` table is parsed and filtered based on tags, and additional actions like sorting by frequency of use or updating user status can be added.

## TODOs

1. **Compare with User's Current Reading List**  
   - Remove any cards the user has already seen.
   - Update frequency of review for cards the user has marked as difficult or reviewed.

2. **Refresh User's Main Deck**  
   - Allow the user to refresh individual characters, especially those marked as "hard."

3. **Support Multiple Deck Types**  
   - Add support for compound words or decks of mixed content types.

4. **Enhance Sorting and Filtering**  
   - Order cards by frequency of use, ensuring the most frequent characters are always at the top for review.

## Conclusion

This offers a flexible framework for handling Anki decks, particularly focused on character categorization. By utilizing SQLite and the Anki database structure, users can automate the process of deck modification, character sorting, and integration with AnkiDroid for seamless learning and review management.