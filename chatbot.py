#Agente
from utils import *
from logic import * 

#Knowledge Base 

clauses = []

#René 
clause.append(expr("(Sintoma(x, Enrojecimiento) & Sintoma(x, PielInflamada) & Sintoma(x, PielSensible) & Sintoma(x, Ardor) & Sintoma(x, Brotes)) ==> Enfermo(x, RosaceaT1)"))
clause.append(expr("(Sintoma(x, Enrojecimiento) & Sintoma(x, PielSensible) & Sintoma(x, PielGraso) & Sintoma(x, Brotes)) ==> Enfermo(x, RosaceaT2)"))
clause.append(expr("(Sintoma(x, Enrojecimiento) & Sintoma(x, PorosDilatados) & Sintoma(x, PielGraso) & Sintoma(x, Bultos)) ==> Enfermo(x, RosaceaT3)"))
clause.append(expr("(Sintoma(x, Enrojecimiento) & Sintoma(x, OjosLacrimosos) & Sintoma(x, OjosIrritados) & Sintoma(x, OjosEnrojecidos) & Sintoma(x, VisionBorrosa)) ==> Enfermo(x, RosaceaT4)"))
clause.append(expr("Enfermo(x, RosaceaT1) ==> Recomendar(x, Demodex)"))
clause.append(expr("Enfermo(x, RosaceaT2) ==> Recomendar(x, Demodex)"))
clause.append(expr("Enfermo(x, RosaceaT3) ==> Recomendar(x, Demodex)"))
clause.append(expr("Enfermo(x, RosaceaT4) ==> Recomendar(x, Demodex)"))
clause.append(expr("Enfermo(x, RosaceaT1) ==> Recomendar(x, Demodex)"))
clause.append(expr("Enfermo(x, RosaceaT1) ==> Tratamiento(x, CremaMetronidazol)"))
clause.append(expr("Enfermo(x, RosaceaT2) ==> Tratamiento(x, CremaMetronidazol)"))
clause.append(expr("Enfermo(x, RosaceaT3) ==> Tratamiento(x, CremaMetronidazol)"))
clause.append(expr("Enfermo(x, RosaceaT4) ==> Tratamiento(x, CremaMetronidazol)"))
clause.append(expr("Enfermo(x, RosaceaT1) ==> Tratamiento(x, CremaAcidoZelaico)"))
clause.append(expr("Enfermo(x, RosaceaT2) ==> Tratamiento(x, CremaAcidoZelaico)"))
clause.append(expr("Enfermo(x, RosaceaT3) ==> Tratamiento(x, CremaAcidoZelaico)"))
clause.append(expr("Enfermo(x, RosaceaT4) ==> Tratamiento(x, CremaAcidoZelaico)"))
clause.append(expr("Enfermo(x, RosaceaT1) ==> Tratamiento(x, CremaRetinoides)"))
clause.append(expr("Enfermo(x, RosaceaT2) ==> Tratamiento(x, CremaRetinoides)"))
clause.append(expr("Enfermo(x, RosaceaT3) ==> Tratamiento(x, CremaRetinoides)"))
clause.append(expr("Enfermo(x, RosaceaT4) ==> Tratamiento(x, CremaRetinoides)"))
clause.append(expr("Enfermo(x, RosaceaT1) ==> Tratamiento(x, OralDoxiciclina)"))
clause.append(expr("Enfermo(x, RosaceaT2) ==> Tratamiento(x, OralDoxiciclina)"))
clause.append(expr("Enfermo(x, RosaceaT3) ==> Tratamiento(x, OralDoxiciclina)"))
clause.append(expr("Enfermo(x, RosaceaT4) ==> Tratamiento(x, OralDoxiciclina)"))
clause.append(expr("(Sintoma(x, Picor) & Sintoma(x, Surcos) & Sintoma(x, PicorConocidos)) ==> Enfermo(x, Sarna)"))
clause.append(expr("Enfermo(x, Sarna) ==> Recomendar(x, Biopsia)"))
clause.append(expr("Enfermo(x, Sarna) ==> Tratamiento(x, Antihistaminico)"))
clause.append(expr("Enfermo(x, Sarna) ==> Tratamiento(x, Permetrina)"))
clause.append(expr("Sintoma(x, Telarana) ==> Enfermo(x, Telangeictasias)"))
clause.append(expr("Enfermo(x, Telangeictasias) ==> Recomendar(x, NoSol)"))
clause.append(expr("Enfermo(x, Telangeictasias) ==> Tratamiento(x, Escleroterapia)"))
clause.append(expr("(Sintoma(x, RonchasRojas) & Sintoma(x, Erupcion) & Sintoma(x, FiebreAlta)) ==> Enfermo(x, Taxicodermia)"))
clause.append(expr("Enfermo(x, Taxicodermia) ==> Tratamiento(x, NoMedicamentos)"))
clause.append(expr("(Sintoma(x, Picor) & Sintoma(x, Hinchazon) & Sintoma(x, Enrojecimiento) & Sintoma(x, RonchaRojas)) ==> Enfermo(x, Urticaria)"))
clause.append(expr("Enfermo(x, Urticaria) ==> Tratamiento(x, Corticoides)"))
clause.append(expr("Enfermo(x, Urticaria) ==> Tratamiento(x, Antihistaminico)"))


doctor_kb = FolKB(clauses)

######## Preguntas 

name = input("¿Cual es tu nombre? ")

if (input("¿Tienes enrojecimiento en la piel? ").lower() == 's'): 
    doctor_kb.tell(expr("Sintoma({}, Enrojecimiento)".format(name)))

if (input("¿Presenta Fiebre? ").lower() == 's'): 
    doctor_kb.tell(expr("Sintoma({}, Fiebre)".format(name))) 

if (input("¿Presenta Picor? ").lower() == 's'): 
    doctor_kb.tell(expr("Sintoma({}, Picor)".format(name)))

if (input("¿Presenta hinchazon? ").lower() == 's'): 
    doctor_kb.tell(expr("Sintoma({}, Hinchazon)".format(name))) 

if (input("¿Presenta ojos irritados? ").lower() == 's'): 
    doctor_kb.tell(expr("Sintoma({}, OjosIrritados)".format(name))) 

if (input("¿Presenta ojos lacrimosos? ").lower() == 's'): 
    doctor_kb.tell(expr("Sintoma({}, OjosLacrimosos)".format(name))) 

if (input("¿Presenta ojos enrojecidos? ").lower() == 's'): 
    doctor_kb.tell(expr("Sintoma({}, OjosEnrojecidos)".format(name))) 

if (input("¿Presenta vision borrosa? ").lower() == 's'): 
    doctor_kb.tell(expr("Sintoma({}, VisionBorrosa)".format(name))) 

if (input("¿Presenta telarañas en la piel? ").lower() == 's'): 
    doctor_kb.tell(expr("Sintoma({}, Telarana)".format(name))) 


### Tratamiento 
print("\n Este es el tratamiento a llevar \n")
answer = fol_fc_ask(doctor_kb, expr("Tratamiento({}, x)".format(name)))
answer = list(answer)

if len(answer) > 0: 
    for sintoms in answer: 
        print(sintoms[x])

else: 
    print("No hay diagnostico")

