"""
Author: Tainah Correia Barreto
"""

print("Bem-vindo ao jogo dos Anti-Néfi-Leítas!")
print("Você está em uma terra distante.")

resposta1 = input("Você quer seguir o caminho da paz ou o caminho da guerra? (PAZ / GUERRA)")

if resposta1 == "PAZ":
    print("Você escolheu o caminho da paz.")
    resposta2 = input("Você quer ajudar os Anti-Néfi-Leítas ou se juntar aos Lamanitas? (AJUDAR / JUNTAR)")

    if resposta2 == "AJUDAR":
        print("Você decide ajudar os Anti-Néfi-Leítas.")
        resposta3 = input("Você quer pregar o evangelho ou construir uma cidade? (PREGAR / CONSTRUIR)")

        if resposta3 == "PREGAR":
            print("Você prega o evangelho e muitas pessoas se convertem.")
            print("Parabéns, você venceu o jogo!")

        else resposta3 == "CONSTRUIR":
            print("Você constrói uma cidade próspera para os Anti-Néfi-Leítas.")
            print("Parabéns, você venceu o jogo!")

    elif resposta2 == "JUNTAR":
        print("Você decide se juntar aos Lamanitas.")
        resposta4 = input("Você quer lutar contra os Anti-Néfi-Leítas ou se arrepender? (LUTAR / ARREPENDER)")

        if resposta4 == "LUTAR":
            print("Você luta contra os Anti-Néfi-Leítas e perde a batalha.")
            print("Infelizmente, você perdeu o jogo.")

        elif resposta4 == "ARREPENDER":
            print("Você se arrepende e abandona a guerra.")
            print("Parabéns, você venceu o jogo!")

elif resposta1 == "GUERRA":
    print("Você escolheu o caminho da guerra.")
    resposta5 = input("Você quer liderar os Lamanitas ou se juntar aos Nefitas? (LIDERAR / JUNTAR)")

    if resposta5 == "LIDERAR":
        print("Você se torna um líder poderoso dos Lamanitas.")
        resposta6 = input("Você quer conquistar territórios ou fazer um tratado de paz? (CONQUISTAR / TRATADO)")

        if resposta6 == "CONQUISTAR":
            print("Você conquista muitos territórios, mas a guerra continua.")
            print("Infelizmente, você perdeu o jogo.")

        elif resposta6 == "TRATADO":
            print("Você faz um tratado de paz e encerra a guerra.")
            print("Parabéns, você venceu o jogo!")

    elif resposta5 == "JUNTAR":
        print("Você decide se juntar aos Nefitas.")
        resposta7 = input("Você quer lutar pela liberdade ou trair os Nefitas? (LUTAR / TRAIR)")

        if resposta7 == "LUTAR":
            print("Você luta pela liberdade e ajuda os Nefitas a vencerem a guerra.")
            print("Parabéns, você venceu o jogo!")

        elif resposta7 == "TRAIR":
            print("Você trai os Nefitas e é derrotado.")
            print("Infelizmente, você perdeu o jogo.")

print("Obrigado por jogar!")
