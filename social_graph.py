from datasets.message import message
import json
'''def write_in_xlsx(filename="default.xlsx",matrix_data):
    try:
        new_social_netword_matrix = xlsxwriter.Workbook(filename)
        worksheet = new_social_netword_matrix.add_worksheet()
        if new_social_netword_matrix:
            for row in range(len(matrix_data)-1):
                for col in range(len(matrix_data[row])-1):
                    worksheet.write(row, col, matrix_data[row][col])
        
        new_social_netword_matrix.close()
        print('le fichier a ete ecrit avec succes')
    except:
        print('Aucun fichier de cet type')
'''
def contract(message):
    #decoded_msg = message.decode('utf8')
    type_message = message['type']
    recipient_list = message['recipient']
    recipientable = []
    for recipient in recipient_list:
        #densite du groupe
        dg = recipient.dencity()
        #statut du groupe
        sg = recipient.get_status_value()
        #Degre moyen du groupe
        svgdg = recipient.community_degre()
        #capacité d'acceptation de canulas
        cg = recipient.acceptation_capacity()
        #type de sujet abordé
        tg = recipient.type_subject(type_message=type_message)
    
        rho = dg + sg + svgdg + cg + tg
        recipient.transactions += 1
        recipient.rho = rho
        #print(rho)
        if rho > 0.75:
            recipient.accepted_msg += 1
            recipientable.append(recipient)

    return recipientable

if __name__== '__main__':
    
    contrat = contract(message)
    
    for i, g in enumerate(contrat):
        print("{} : {}".format(i, g.rho))