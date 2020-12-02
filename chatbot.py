# -*- coding: utf-8 -*-
import re

# Lista de intenções e sinônimos
intent_synonym = {
    'saudacao': ('.*\\boi\\b.*|.*\\bola\\b.*|.*\\bbom dia\\b.*|.*\\bboa tarde\\b.*|.*\\bboa noite\\b.*|.*\\bsalve\\b.*|.*\\btudo bem?\\b.*'),
    'funcionamento': ('.*\\bhorario\\b.*|.*\\bfuncionamento\\b.*|.*\\baberto\\b.*|.*\\babertos\\b.*|.*\\bfechado\\b.*|.*\\bfechados\\b.*'),
    'pagamento': ('.*\\bcartao\\b.*|.*\\bcredito\\b.*|.*\\bdebito\\b.*|.*\\bdinheiro\\b.*|.*\\bcheque\\b.*|.*\\bpagamento\\b.*|.*\\bpagar\\b.*|.*\\bvr\\b.*|.*\\bvale\\b.*|.*\\bvale-refeicao\\b.*'),
    'reclamacao': ('.*\\breclamar\\b.*|.*\\breclamacao\\b.*|.*\\bdenunciar\\b.*'),
    'cardapio': ('.*\\bcardapio\\b.*|.*\\bmenu\\b.*|.*\\bopcoes\\b.*|.*\\bpratos\\b.*')
}

# Lista de respostas por intenção
responses = {
    'saudacao':'\nOlá! Como posso te ajudar?\n',
    'funcionamento':'\nEstamos abertos de 9AM à 5PM, de Segunda à Sexta. Fechamos aos finais de semana e feriados nacionais.\n',
    'confusao':'\nDesculpe, não entendi. Você pode repetir?\n',
    'pagamento':'\nNós aceitamos todos os cartões de crédito/débito, dinheiro e vale-refeição\n',
    'reclamacao':'\nPara registrar uma reclamação ou denúncia, telefone ou envie uma mensagem para o número 91234-5678\n',
    'cardapio':'\nHamburguer 100g - R$ 20.99\nHamburguer 180g - R$ 34.99\nRefrigerante 350ml - R$ 2.75\nFritas - R$ 6.79\n'
}

print("Este é o Hamburguer do Cardoso. Como posso te ajudar?")

# Inicia o ciclo do bot
while (True):  
    
    # Aceita a entrada do usuário e converte para lowercase
    user_input = str(raw_input()).lower()
    
    # Define a condição de saída do bot
    if user_input == 'tchau': 
        print ("Obrigado pela visita. Volte sempre.")
        break
    

    intent_matched = None 
    
    for intent,expression in intent_synonym.items():
        if re.search(expression, user_input):
            
            # Se uma expressão dá match, seleciona a intenção correspondente no dicionário de intenções
            intent_matched = intent
        
    # Caso o bot não compreenda a expressão
    key = 'confusao' 
    if intent_matched in responses:
        
        # Caso o bot compreenda, a resposta confusa é substituida pela intenção correspondente à entrada do usuário
        key = intent_matched
    
    # O bot imprime na tela a resposta adequada
    print (responses[key])