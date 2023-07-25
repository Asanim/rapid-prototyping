
from ankisync2 import Apkg

apkg = Apkg("./Most_Common_3000_Chinese_Hanzi_Characters.apkg")

for card in apkg:
    print(card)



# with Apkg("example.apkg") as apkg:
#     m = apkg.db.Models.create(name="foo", flds=["field1", "field2"])
#     d = apkg.db.Decks.create(name="bar::baz")
#     t = [
#         apkg.db.Templates.create(name="fwd", mid=m.id, qfmt="{{field1}}", afmt="{{field2}}"),
#         apkg.db.Templates.create(name="bwd", mid=m.id, qfmt="{{field2}}", afmt="{{field1}}")
#     ]
#     n = apkg.db.Notes.create(mid=m.id, flds=["data1", "<img src='media.jpg'>"], tags=["tag1", "tag2"])
#     c = [
#         apkg.db.Cards.create(nid=n.id, did=d.id, ord=i)
#         for i, _ in enumerate(t)
#     ]