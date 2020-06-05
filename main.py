from classes.class_refletiva import refletiva
from classes.class_flash import flash
from classes.class_entrepista import entrepista
from classes.class_chuva_neblina import chuv_nebli
from classes.class_fosca import fosca
from classes.class_relatorio import Relatorio

obj = flash('Análise Completa 08-04.csv')

obj2 = refletiva('Análise Completa 08-04.csv')

obj3 = entrepista('Análise Completa 08-04.csv')

obj4 = chuv_nebli('Análise Completa 08-04.csv')

obj5 = fosca('Análise Completa 08-04.csv')

"""print(obj.with_problem())
print(obj2.with_problem())
print(obj3.with_problem())
print(obj4.with_problem())
print(obj5.with_problem())


print(obj.confusion_matrix())
print(obj2.confusion_matrix())
print(obj3.confusion_matrix())
print(obj4.confusion_matrix())
print(obj5.confusion_matrix())


print(obj.classification())
print(obj2.classification())
print(obj3.classification())
print(obj4.classification())
print(obj5.classification())"""

"""print(obj5.with_problem())
print(obj5.classification())
print(obj5.confusion_matrix())"""

relatorio = Relatorio('Análise Completa 08-04.csv')
relatorio.geral()