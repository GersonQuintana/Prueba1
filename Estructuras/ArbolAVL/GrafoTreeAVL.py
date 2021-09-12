from subprocess import check_call

class GrafoABB:

    def __init__(self):
        self.contInser = 0

    
    def graficarArbol(self, arbol):
        acumuladores = ["digraph G{\nnode [shape=record, height=.1];\n", ""]

        if arbol.root != None:
            self.recorrerArbol(arbol.root, acumuladores)
        
        filename = ""
        

        self.contInser = self.contInser + 1
        filename = "insercion.dot"

        acumuladores[0] += acumuladores[1] + "\n}"
        archivo = open(filename, "w")
        archivo.write(acumuladores[0])
        archivo.close()

        check_call(['dot','-Tpng',filename,'-o', 'insercion.png'])

        


    def recorrerArbol(self, raiz,acum):

        if raiz:
            nombre = raiz.estudiante.getNombre().replace("\"", "")
            carrera = raiz.estudiante.getCarrera().replace("\"", "")
            acum[0] += "\"" + str(hash(raiz)) + "\"" + "[label=\" <f0> | { { <f1> " + str(raiz.key) + " } | { " + nombre + " } |  {" + carrera + " } } | <f2>\"];\n"
            # acum[0] += '"{}"[label=" <f0> | { <f1> {} | }| <f2>"];\n'.format(str(hash(raiz)), str(raiz.key))

            if raiz.izq != None:
                acum[1] += '"{}":f0 -> "{}":f1;\n'.format(str(hash(raiz)), str(hash(raiz.izq)))
            if raiz.der != None:
                acum[1] += '"{}":f2 -> "{}":f1;\n'.format(str(hash(raiz)), str(hash(raiz.der)))

            self.recorrerArbol(raiz.izq, acum)
            self.recorrerArbol(raiz.der, acum)


#             node [shape = record,height=.1];
# node0[label = "<f0> |<f1> G|<f2> "];
# node1[label = "<f0> |<f1> E|<f2> "];
# node2[label = "<f0> |<f1> B|<f2> "];
# node3[label = "<f0> |<f1> F|<f2> "];
# node4[label = "<f0> |<f1> R|<f2> "];
# node5[label = "<f0> |<f1> H|<f2> "];
# node6[label = "<f0> |<f1> Y|<f2> "];
# node7[label = "<f0> |<f1> A|<f2> "];
# node8[label = "<f0> |<f1> C|<f2> "];
# "node0":f2 -> "node4":f1;
# "node0":f0 -> "node1":f1;
# "node1":f0 -> "node2":f1;
# "node1":f2 -> "node3":f1;
# "node2":f2 -> "node8":f1;
# "node2":f0 -> "node7":f1;
# "node4":f2 -> "node6":f1;
# "node4":f0 -> "node5":f1;


# digraph G{
# node [shape=circle];
# "164152271686"[label="12345678"];
# "164152271803"[label="1"];
# "164152271848"[label="0"];
# "164152271809"[label="2"];
# "164152271797"[label="201901425"];
# "164152271815"[label="201501786"];
# "164152271779"[label="201001786"];
# "164152271863"[label="201822186"];
# "164152271866"[label="201908686"];
# "164152271686" -> "164152271803";
# "164152271686" -> "164152271797";
# "164152271803" -> "164152271848";
# "164152271803" -> "164152271809";
# "164152271797" -> "164152271815";
# "164152271797" -> "164152271866";
# "164152271815" -> "164152271779";
# "164152271815" -> "164152271863";

# }