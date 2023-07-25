This repo contains code of reading and categorizing characters for later use in AnkiDroid.


https://github.com/ankidroid/Anki-Android/wiki/Database-Structure

├── example
│   ├── example.anki2
│   └── media
└── example.apkg
In linux sqliteman or sqlite3 can be used to read and modify the .anki2 files.


## Test 2
python code to unzip an anki apkg file like Chinese_Radicals_100.apkg, then parse the sqlite database in anki version 2 format. I want to create a copy of the sqlitedb, delete all items in the copy, keeping only the tables then sort through the original database and copy a few entires in one by one. Please provide example code to do this


col = user settings

```
-- Notes contain the raw information that is formatted into a number of cards
-- according to the models
CREATE TABLE notes (
    id              integer primary key,
      -- epoch milliseconds of when the note was created
    guid            text not null,
      -- globally unique id, almost certainly used for syncing
    mid             integer not null,
      -- model id
    mod             integer not null,
      -- modification timestamp, epoch seconds
    usn             integer not null,
      -- update sequence number: for finding diffs when syncing.
      --   See the description in the cards table for more info
    tags            text not null,
      -- space-separated string of tags. 
      --   includes space at the beginning and end, for LIKE "% tag %" queries
    flds            text not null,
      -- the values of the fields in this note. separated by 0x1f (31) character.
    sfld            integer not null,
      -- sort field: used for quick sorting and duplicate check. The sort field is an integer so that when users are sorting on a field that contains only numbers, they are sorted in numeric instead of lexical order. Text is stored in this integer field.
    csum            integer not null,
      -- field checksum used for duplicate check.
      --   integer representation of first 8 digits of sha1 hash of the first field
    flags           integer not null,
      -- unused
    data            text not null
      -- unused
);
```

(1453219106197, 'o_4h`pop|W', 1453218888792, 1457014305, 0, '', '人\x1f人\x1f亻&nbsp;\x1f\x1fhuman, person, people\x1frén\x1fNote similarity to 八, which means eight.&nbsp;\x1f今仁休位他\x1f[sound:pronunciation_zh_人.mp3]', '人', 1225946906, 0, '')

Keep all the same, copy only the Cards table!!!
set all lvl and user information back to false 
copy only the cards that have the same id as the given text 
Order by frequency of use such that the most frequent characters alway appear first

TODO:
compare with the user's current readling list, removing all cards that the user has already seen. 
    updating frequency of review for ones that are?
    or perhaps allow the user to have a quick refersh of each individual character. ANY that have been marked hard are refreshed in the user's main deck!

This is the main repo from which the user has a collection of all their cards

TODO:
support different deck types and allow compund words if possible


'人'