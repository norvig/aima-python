#Agente
from utils import *
from logic import * 

#Knowledge Base 

clauses = []

#René 
clauses.append(expr("(Sintoma(x, Enrojecimiento) & Sintoma(x, PielInflamada) & Sintoma(x, PielSensible) & Sintoma(x, Ardor) & Sintoma(x, Brotes)) ==> Enfermo(x, RosaceaT1)"))
clauses.append(expr("(Sintoma(x, Enrojecimiento) & Sintoma(x, PielSensible) & Sintoma(x, PielGraso) & Sintoma(x, Brotes)) ==> Enfermo(x, RosaceaT2)"))
clauses.append(expr("(Sintoma(x, Enrojecimiento) & Sintoma(x, PorosDilatados) & Sintoma(x, PielGraso) & Sintoma(x, Bultos)) ==> Enfermo(x, RosaceaT3)"))
clauses.append(expr("(Sintoma(x, Enrojecimiento) & Sintoma(x, OjosLacrimosos) & Sintoma(x, OjosIrritados) & Sintoma(x, OjosEnrojecidos) & Sintoma(x, VisionBorrosa)) ==> Enfermo(x, RosaceaT4)"))
clauses.append(expr("Enfermo(x, RosaceaT1) ==> Recomendar(x, Demodex)"))
clauses.append(expr("Enfermo(x, RosaceaT2) ==> Recomendar(x, Demodex)"))
clauses.append(expr("Enfermo(x, RosaceaT3) ==> Recomendar(x, Demodex)"))
clauses.append(expr("Enfermo(x, RosaceaT4) ==> Recomendar(x, Demodex)"))
clauses.append(expr("Enfermo(x, RosaceaT1) ==> Recomendar(x, Demodex)"))
clauses.append(expr("Enfermo(x, RosaceaT1) ==> Tratamiento(x, CremaMetronidazol)"))
clauses.append(expr("Enfermo(x, RosaceaT2) ==> Tratamiento(x, CremaMetronidazol)"))
clauses.append(expr("Enfermo(x, RosaceaT3) ==> Tratamiento(x, CremaMetronidazol)"))
clauses.append(expr("Enfermo(x, RosaceaT4) ==> Tratamiento(x, CremaMetronidazol)"))
clauses.append(expr("Enfermo(x, RosaceaT1) ==> Tratamiento(x, CremaAcidoZelaico)"))
clauses.append(expr("Enfermo(x, RosaceaT2) ==> Tratamiento(x, CremaAcidoZelaico)"))
clauses.append(expr("Enfermo(x, RosaceaT3) ==> Tratamiento(x, CremaAcidoZelaico)"))
clauses.append(expr("Enfermo(x, RosaceaT4) ==> Tratamiento(x, CremaAcidoZelaico)"))
clauses.append(expr("Enfermo(x, RosaceaT1) ==> Tratamiento(x, CremaRetinoides)"))
clauses.append(expr("Enfermo(x, RosaceaT2) ==> Tratamiento(x, CremaRetinoides)"))
clauses.append(expr("Enfermo(x, RosaceaT3) ==> Tratamiento(x, CremaRetinoides)"))
clauses.append(expr("Enfermo(x, RosaceaT4) ==> Tratamiento(x, CremaRetinoides)"))
clauses.append(expr("Enfermo(x, RosaceaT1) ==> Tratamiento(x, OralDoxiciclina)"))
clauses.append(expr("Enfermo(x, RosaceaT2) ==> Tratamiento(x, OralDoxiciclina)"))
clauses.append(expr("Enfermo(x, RosaceaT3) ==> Tratamiento(x, OralDoxiciclina)"))
clauses.append(expr("Enfermo(x, RosaceaT4) ==> Tratamiento(x, OralDoxiciclina)"))
clauses.append(expr("(Sintoma(x, Picor) & Sintoma(x, Surcos) & Sintoma(x, PicorConocidos)) ==> Enfermo(x, Sarna)"))
clauses.append(expr("Enfermo(x, Sarna) ==> Recomendar(x, Biopsia)"))
clauses.append(expr("Enfermo(x, Sarna) ==> Tratamiento(x, Antihistaminico)"))
clauses.append(expr("Enfermo(x, Sarna) ==> Tratamiento(x, Permetrina)"))
clauses.append(expr("Sintoma(x, Telarana) ==> Enfermo(x, Telangeictasias)"))
clauses.append(expr("Enfermo(x, Telangeictasias) ==> Recomendar(x, NoSol)"))
clauses.append(expr("Enfermo(x, Telangeictasias) ==> Tratamiento(x, Escleroterapia)"))
clauses.append(expr("(Sintoma(x, RonchasRojas) & Sintoma(x, Erupcion) & Sintoma(x, FiebreAlta)) ==> Enfermo(x, Taxicodermia)"))
clauses.append(expr("Enfermo(x, Taxicodermia) ==> Tratamiento(x, NoMedicamentos)"))
clauses.append(expr("(Sintoma(x, Picor) & Sintoma(x, Hinchazon) & Sintoma(x, Enrojecimiento) & Sintoma(x, RonchaRojas)) ==> Enfermo(x, Urticaria)"))
clauses.append(expr("Enfermo(x, Urticaria) ==> Tratamiento(x, Corticoides)"))
clauses.append(expr("Enfermo(x, Urticaria) ==> Tratamiento(x, Antihistaminico)"))
clauses.append(expr("Sintoma(x, Fiebre) ==> Tratamiento(x, Paracetamol)"))
clauses.append(expr("Sintoma(x, FiebreAlta) ==> Tratamiento(x, Paracetamol)"))

#Maria Paula
#clauses.append(expr(""))
clauses.append(expr("Sintoma(x, PuntosBlancos) ==> Enfermo(x, Acne)"))
clauses.append(expr("(Sintoma(x, PuntosBlancos) & Sintoma(x, PuntosNegros) & Sintoma(x, Papulas)) ==> Enfermo(x, Acne)"))
clauses.append(expr("Sintoma(x, Papulas) ==> Enfermo(x, Acne)"))
clauses.append(expr("(Sintoma(x, PuntosBlancos) & Sintoma(x, Papulas) & Sintoma(x, Seborrea)) ==> Enfermo(x, Acne)"))
clauses.append(expr("(Sintoma(x, PuntosBlancos) & Sintoma(x, PuntosNegros) & Sintoma(x, Papulas) & Sintoma(x, Seborrea)) ==> Enfermo(x, Acne)"))
clauses.append(expr("Enfermo(x, Acne) ==> Tratamiento(Clindamicina)"))
clauses.append(expr("Enfermo(x, Acne) ==> Tratamiento(x, GelPeroxidoBenzoilo)"))
clauses.append(expr("Enfermo(x, Acne) ==> Tretinoina"))
clauses.append(expr("(Sintoma(x, Vesiculas) & Sintoma(x, DolorBoca) & Sintoma(x, Fiebre)) ==> Enfermo(x, Herpes)"))
clauses.append(expr("(Sintoma(x, Vesiculas) & Sintoma(x, Fiebre)) ==> Enfermo(x, Herpes)"))
clauses.append(expr("(Sintoma(x, Vesiculas) & Sintoma(x, DolorBoca)) ==> Enfermo(x, Herpes)"))

# Gabriela Lujan

# Tratamientos
clauses.append(expr("Enfermedad(x, Melasma) ==> Tratamiento(x, ProtectorSolar)"))
clauses.append(expr("Enfermedad(x, Melasma) ==> Tratamiento(x, CremasTopicas)"))
clauses.append(expr("Enfermedad(x, Melasma) ==> Tratamiento(x, ExfoliacionesQuimicas)"))
clauses.append(expr("Enfermedad(x, Melasma) ==> Tratamiento(x, Laser)"))
clauses.append(expr("Enfermedad(x, Melanoma) ==> Tratamiento(x, ExtirpacionQuirurjica)"))
clauses.append(expr("Enfermedad(x, PitiriasisVersicolor) ==> Tratamiento(x, CremasAntimicoticas)"))
clauses.append(expr("Enfermedad(x, PitiriasisVersicolor) ==> Tratamiento(x, ChampusAntimicoticas)"))
clauses.append(expr("Enfermedad(x, PitiriasisVersicolor) ==> Tratamiento(x, Pastillas Antimicoticas)"))
clauses.append(expr("Enfermedad(x, Psoriasis) ==> Tratamiento(x, CremasTopicas)"))
clauses.append(expr("Enfermedad(x, Psoriasis) ==> Tratamiento(x, Fototrapia)"))
clauses.append(expr("Enfermedad(x, Psoriasis) ==> Tratamiento(x, MedicamentosOrales)"))
clauses.append(expr("Enfermedad(x, Psoriasis) ==> Tratamiento(x, Medicamentos Inyectables)"))

# Recomendaciones
clauses.append(expr("Enfermedad(x, Melasma) ==> Recomendacion(x, MinimiceSol)"))
clauses.append(expr("Enfermedad(x, Melasma) ==> Recomendacion(x, ControlEstres)"))
clauses.append(expr("Enfermedad(x, Melasma) ==> Recomendacion(x, ProductosSinFragancias)"))
clauses.append(expr("Enfermedad(x, Melasma) ==> Recomendacion(x, Dermatologo)"))
clauses.append(expr("Enfermedad(x, Melasma) ==> Recomendacion(x, DietaEquilibrada)"))
clauses.append(expr("Enfermedad(x, Melanoma) ==> Recomendacion(x, DietaEquilibrada)"))
clauses.append(expr("Enfermedad(x, Melanoma) ==> Recomendacion(x, MinimiceSol)"))
clauses.append(expr("Enfermedad(x, Melanoma) ==> Recomendacion(x, ControlEstres)"))
clauses.append(expr("Enfermedad(x, Melanoma) ==> Recomendacion(x, Dermatologo)"))
clauses.append(expr("Enfermedad(x, Melanoma) ==> Recomendacion(x, ExaminePiel)"))
clauses.append(expr("Enfermedad(x, Melanoma) ==> Recomendacion(x, NoFumar)"))
clauses.append(expr("Enfermedad(x, Melanoma) ==> Recomendacion(x, Segumiento)"))
clauses.append(expr("Enfermedad(x, PitiriasisVersicolor) ==> Recomendacion(x, DietaEquilibrada)"))
clauses.append(expr("Enfermedad(x, PitiriasisVersicolor) ==> Recomendacion(x, MinimiceSol)"))
clauses.append(expr("Enfermedad(x, PitiriasisVersicolor) ==> Recomendacion(x, MinimiceCalor)"))
clauses.append(expr("Enfermedad(x, Psoriasis) ==> Recomendacion(x, DietaEquilibrada)"))
clauses.append(expr("Enfermedad(x, Psoriasis) ==> Recomendacion(x, ControlEstres)"))
clauses.append(expr("Enfermedad(x, Psoriasis) ==> Recomendacion(x, NoFumar)"))

# Sintomas
clauses.append(expr("Sintoma(x, ParcheMarron) & Sintoma(x, ParcheMejilla) & Sintoma(x, NoMolestia) ==> Enfermedad(x, Melasma)"))
clauses.append(expr("Sintoma(x, ParcheMarron) & Sintoma(x, ParcheFrente) & Sintoma(x, NoMolestia) ==> Enfermedad(x, Melasma)"))
clauses.append(expr("Sintoma(x, ParcheMarron) & Sintoma(x, ParchePuenteNariz) & Sintoma(x, NoMolestia) ==> Enfermedad(x, Melasma)"))
clauses.append(expr("Sintoma(x, ParcheMarron) & Sintoma(x, ParcheLabioSuperior) & Sintoma(x, NoMolestia) ==> Enfermedad(x, Melasma)"))
clauses.append(expr("Sintoma(x, ParcheMarron) & Sintoma(x, ParcheMenton) & Sintoma(x, NoMolestia) ==> Enfermedad(x, Melasma)"))
clauses.append(expr("Sintoma(x, CambioLunar) & Sintoma(x, Asimetria) & Sintoma(x, Borde) & Sintoma(x, Color) & Sintoma(x, Diametro) & Sintoma(x, Evolucion) ==> Enfermedad(x, Melanoma)"))
clauses.append(expr("Sintoma(x, SurgeLunar) & Sintoma(x, Asimetria) & Sintoma(x, Borde) & Sintoma(x, Color) & Sintoma(x, Diametro) & Sintoma(x, Evolucion) ==> Enfermedad(x, Melanoma)"))
clauses.append(expr("Sintoma(x, CambioLunar) & Sintoma(x, Asimetria) & Sintoma(x, Borde) & Sintoma(x, Color) & Sintoma(x, Diametro) & Sintoma(x, Evolucion) & Sintoma(x, Dolor) ==> Enfermedad(x, Melanoma)"))
clauses.append(expr("Sintoma(x, SurgeLunar) & Sintoma(x, Asimetria) & Sintoma(x, Borde) & Sintoma(x, Color) & Sintoma(x, Diametro) & Sintoma(x, Evolucion) & Sintoma(x, Dolor) ==> Enfermedad(x, Melanoma)"))
clauses.append(expr("Sintoma(x, ParcheMarron) & Sintoma(x, ParchePecho) & Sintoma(x, NoMolestia) ==> Enfermedad(x, PitiriasisVersicolor)"))
clauses.append(expr("Sintoma(x, ParcheMarron) & Sintoma(x, ParcheEspalda) & Sintoma(x, NoMolestia) ==> Enfermedad(x, PitiriasisVersicolor)"))
clauses.append(expr("Sintoma(x, ParcheMarron) & Sintoma(x, ParcheHombros) & Sintoma(x, NoMolestia) ==> Enfermedad(x, PitiriasisVersicolor)"))
clauses.append(expr("Sintoma(x, ParcheMarron) & Sintoma(x, ParcheSuperiorBrazos) & Sintoma(x, NoMolestia) ==> Enfermedad(x, PitiriasisVersicolor)"))
clauses.append(expr("Sintoma(x, ParcheMarron) & Sintoma(x, ParcheCabeza) & Sintoma(x, NoMolestia) ==> Enfermedad(x, PitiriasisVersicolor)"))
clauses.append(expr("Sintoma(x, ParcheMarron) & Sintoma(x, ParcheAbdomen) & Sintoma(x, NoMolestia) ==> Enfermedad(x, PitiriasisVersicolor)"))
clauses.append(expr("Sintoma(x, ParcheRosa) & Sintoma(x, ParchePecho) & Sintoma(x, NoMolestia) ==> Enfermedad(x, PitiriasisVersicolor)"))
clauses.append(expr("Sintoma(x, ParcheRosa) & Sintoma(x, ParcheEspalda) & Sintoma(x, NoMolestia) ==> Enfermedad(x, PitiriasisVersicolor)"))
clauses.append(expr("Sintoma(x, ParcheRosa) & Sintoma(x, ParcheHombros) & Sintoma(x, NoMolestia) ==> Enfermedad(x, PitiriasisVersicolor)"))
clauses.append(expr("Sintoma(x, ParcheRosa) & Sintoma(x, ParcheSuperiorBrazos) & Sintoma(x, NoMolestia) ==> Enfermedad(x, PitiriasisVersicolor)"))
clauses.append(expr("Sintoma(x, ParcheRosa) & Sintoma(x, ParcheCabeza) & Sintoma(x, NoMolestia) ==> Enfermedad(x, PitiriasisVersicolor)"))
clauses.append(expr("Sintoma(x, ParcheRosa) & Sintoma(x, ParcheAbdomen) & Sintoma(x, NoMolestia) ==> Enfermedad(x, PitiriasisVersicolor)"))
clauses.append(expr("Sintoma(x, ParcheRojo) & Sintoma(x, ParchePecho) & Sintoma(x, NoMolestia) ==> Enfermedad(x, PitiriasisVersicolor)"))
clauses.append(expr("Sintoma(x, ParcheRojo) & Sintoma(x, ParcheEspalda) & Sintoma(x, NoMolestia) ==> Enfermedad(x, PitiriasisVersicolor)"))
clauses.append(expr("Sintoma(x, ParcheRojo) & Sintoma(x, ParcheHombros) & Sintoma(x, NoMolestia) ==> Enfermedad(x, PitiriasisVersicolor)"))
clauses.append(expr("Sintoma(x, ParcheRojo) & Sintoma(x, ParcheSuperiorBrazos) & Sintoma(x, NoMolestia) ==> Enfermedad(x, PitiriasisVersicolor)"))
clauses.append(expr("Sintoma(x, ParcheRojo) & Sintoma(x, ParcheCabeza) & Sintoma(x, NoMolestia) ==> Enfermedad(x, PitiriasisVersicolor)"))
clauses.append(expr("Sintoma(x, ParcheRojo) & Sintoma(x, ParcheAbdomen) & Sintoma(x, NoMolestia) ==> Enfermedad(x, PitiriasisVersicolor)"))
clauses.append(expr("Sintoma(x, ParcheBlanco) & Sintoma(x, ParchePecho) & Sintoma(x, NoMolestia) ==> Enfermedad(x, PitiriasisVersicolor)"))
clauses.append(expr("Sintoma(x, ParcheBlanco) & Sintoma(x, ParcheEspalda) & Sintoma(x, NoMolestia) ==> Enfermedad(x, PitiriasisVersicolor)"))
clauses.append(expr("Sintoma(x, ParcheBlanco) & Sintoma(x, ParcheHombros) & Sintoma(x, NoMolestia) ==> Enfermedad(x, PitiriasisVersicolor)"))
clauses.append(expr("Sintoma(x, ParcheBlanco) & Sintoma(x, ParcheSuperiorBrazos) & Sintoma(x, NoMolestia) ==> Enfermedad(x, PitiriasisVersicolor)"))
clauses.append(expr("Sintoma(x, ParcheBlanco) & Sintoma(x, ParcheCabeza) & Sintoma(x, NoMolestia) ==> Enfermedad(x, PitiriasisVersicolor)"))
clauses.append(expr("Sintoma(x, ParcheBlanco) & Sintoma(x, ParcheAbdomen) & Sintoma(x, NoMolestia) ==> Enfermedad(x, PitiriasisVersicolor)"))
clauses.append(expr("Sintoma(x, ParcheRojo) & Sintoma(x, ParcheInflamado) & Sintoma(x, Molestia) & Sintoma(x, ParcheEscamoso) ==> Enfermedad(x, Psoriasis)"))

doctor_kb = FolKB(clauses)

######## Preguntas 

name = input("¿Cual es tu nombre? ")

if (input("¿Tienes enrojecimiento en la piel? ").lower() == 's'): 
    doctor_kb.tell(expr("Sintoma({}, Enrojecimiento)".format(name)))

dec = fol_fc_ask(doctor_kb, expr("Sintoma({}, Enrojecimiento)".format(name)))
dec = list(dec)

if len(dec) > 0: 

    if (input("¿Presenta ojos irritados? ").lower() == 's'): 
        doctor_kb.tell(expr("Sintoma({}, OjosIrritados)".format(name))) 

    if (input("¿Presenta ojos lacrimosos? ").lower() == 's'): 
        doctor_kb.tell(expr("Sintoma({}, OjosLacrimosos)".format(name))) 

    if (input("¿Presenta ojos enrojecidos? ").lower() == 's'): 
        doctor_kb.tell(expr("Sintoma({}, OjosEnrojecidos)".format(name))) 

    if (input("¿Presenta vision borrosa? ").lower() == 's'): 
        doctor_kb.tell(expr("Sintoma({}, VisionBorrosa)".format(name)))

    if (input("¿Presenta piel inflamada? ").lower() == 's'):
        doctor_kb.tell(expr("Sintoma({}, PielInflamada)".format(name)))

    if (input("¿Presenta piel sensible? ").lower() == 's'):
        doctor_kb.tell(expr("Sintoma({}, PielSensible)".format(name)))

    if (input("¿Presenta piel graso? ").lower() == 's'):
        doctor_kb.tell(expr("Sintoma({}, PielGraso)".format(name)))

    if (input("¿Presenta Brotes en la piel? ").lower() == 's'): 
        doctor_kb.tell(expr("Sintoma({}, Brotes)".format(name)))

    if (input("¿Presenta ardor en la piel? ").lower() == 's'): 
        doctor_kb.tell(expr("Sintoma({}, Ardor)".format(name)))

    if (input("¿Presenta poros dilatados? ").lower() == 's'):
        doctor_kb.tell(expr("Sintoma({}, PorosDilatados)".format(name)))

    if (input("¿Presenta bultos? ").lower() == 's'):
        doctor_kb.tell(expr("Sintoma({}, Bultos)".format(name))) 

#----------------------------------
if (input("¿Presenta Fiebre? ").lower() == 's'): 
    doctor_kb.tell(expr("Sintoma({}, Fiebre)".format(name))) 

dec = fol_fc_ask(doctor_kb, expr("Sintoma({}, Fiebre)".format(name)))
dec = list(dec)

if len(dec) > 0: 
    if (input("¿Presentan sus conocidos Fiebre Alta? ").lower() == 's'): 
        doctor_kb.tell(expr("Sintoma({}, FiebreAlta)".format(name)))

#----------------------------------
if (input("¿Presenta Picor? ").lower() == 's'): 
    doctor_kb.tell(expr("Sintoma({}, Picor)".format(name)))

dec = fol_fc_ask(doctor_kb, expr("Sintoma({}, Picor)".format(name)))
dec = list(dec)

if len(dec) > 0: 
    if (input("¿Presentan sus conocidos Picor? ").lower() == 's'): 
        doctor_kb.tell(expr("Sintoma({}, PicorConocidos)".format(name)))

    if (input("¿Tienes surcos en la piel? ").lower() == 's'):
        doctor_kb.tell(expr("Sintoma({}, Surcos)".format(name)))

#----------------------
if (input("¿Presenta hinchazon? ").lower() == 's'): 
    doctor_kb.tell(expr("Sintoma({}, Hinchazon)".format(name))) 

if (input("¿Presenta telaranas en la piel? ").lower() == 's'): 
    doctor_kb.tell(expr("Sintoma({}, Telarana)".format(name))) 

if (input("¿Presenta hinchazon en la piel? ").lower() == 's'): 
    doctor_kb.tell(expr("Sintoma({}, Hinchazon)".format(name)))

if (input("¿Presenta Ronchas Rojas en la piel? ").lower() == 's'): 
    doctor_kb.tell(expr("Sintoma({}, RonchasRojas)".format(name)))


### Tratamiento 
print("\nEste es el tratamiento a llevar: ")
answer_trat = fol_fc_ask(doctor_kb, expr("Tratamiento({}, x)".format(name)))
answer_trat = list(answer_trat)

if len(answer_trat) > 0: 
    for sintoms in answer_trat: 
        print(sintoms[x])

else: 
    print("No hay tratamiento, te vas a morir muajaja")

### Recomendaciones
print("\nEstas son las recomendaciones a llevar: ")
answer_rec = fol_fc_ask(doctor_kb, expr("Recomendacion({}, x)".format(name)))
answer_rec = list(answer_rec)

if len(answer_rec) > 0: 
    for sintoms in answer_rec: 
        print(sintoms[x])

else: 
    print("No hay recomendaciones")

### Diagnostico 
print("\nEste es el diagnostico: ")
answer_di = fol_fc_ask(doctor_kb, expr("Enfermo({}, x)".format(name)))
answer_di = list(answer_di)

if len(answer_di) > 0: 
    for sintoms in answer_di: 
        print(sintoms[x])

else: 
    print("No hay diagnostico")