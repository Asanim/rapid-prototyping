README

you must have an instance of anki with the anki connect addon installed on your machine
https://docs.ankiweb.net/platform/linux/installing.html

otherwise the api will not work!






# Appendix



这个错误提示表明在调用DeleteThingGroup操作时，请求中包含的安全令牌无效。

通常情况下，这个错误是由于使用了无效或过期的安全令牌导致的。安全令牌通常用于验证和授权对AWS（亚马逊网络服务）资源的访问权限。

要解决这个问题，你可以尝试以下步骤：

检查令牌有效性：确保你使用的安全令牌是有效的，并且没有过期。如果你是使用AWS Identity and Access Management (IAM) 创建的访问密钥，可以在AWS控制台的IAM部分进行验证和更新。

检查令牌权限：确保你的安全令牌具有执行DeleteThingGroup操作所需的必要权限。你可以通过IAM角色或用户策略来管理权限。检查相关策略是否正确配置，并包含DeleteThingGroup操作的权限。

检查网络连接：确保你的应用程序能够与AWS服务进行通信，没有任何网络连接问题。检查网络设置、防火墙或代理配置，确保可以正常访问AWS服务。

如果你仍然遇到问题，建议参考AWS官方文档、开发者论坛或联系AWS支持以获取更详细的帮助和指导。

pip install anki

pcakcage into easy to understand by frequency. with most frequent first



string = "安全令牌通常用于验证和授权对"
unique_chars = set(string)



import anki

# Path to the .apkg file
apkg_file = "path/to/your_deck.apkg"

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
