
from os import startfile, system


def generarGraphviz():
    graphviz='''
    digraph L{
    node[shape=box fillcolor="#FFEDBB" style=filled]

    subgraph cluster_p{
        label="Matriz Dispersa"
        bgcolor="#398D9C"
        raiz[label="0,0"]
        edge[dir="both"]
        /*aqui se crean headers de las filas*/
        F1[label="1",group=1];
        F2[label="2",group=1];
        F3[label="3",group=1];
        F4[label="4",group=1];
        F5[label="5",group=1];
        /*aqui enlazamos los nodos de las filas*/
        F1->F2
        F2->F3
        F3->F4
        F4->F5
        C1[label="1",group=2,fillcolor=yellow];
        C2[label="2",group=3,fillcolor=yellow];
        C3[label="3",group=4,fillcolor=yellow];
        C4[label="4",group=5,fillcolor=yellow];
        C5[label="5",group=6,fillcolor=yellow];
        /* Aqui enlazar los nodos de las cabeceras*/
        C1->C2
        C2->C3
        C3->C4
        C4->C5
        /*UNIR LA RAIZ A LAS FILAS Y COLUMNAS*/
        raiz->F1
        raiz->C1
        /*aqui alineamos cada nodo cabecera de las columnas*/
        {rank=same;raiz;C1;C2;C3,C4,C5}
        nodo1_1[label="1,1",fillcolor=green,group=2]
        nodo4_4[label="4,4",fillcolor=green,group=5]
        nodo5_3[label="5,3",fillcolor=green,group=4]
        nodo2_2[label="2,2",fillcolor=green,group=3]
        nodo2_4[label="2,4",fillcolor=green,group=5]
        nodo3_4[label="3,4",fillcolor=green,group=5]
        nodo5_5[label="5,5",fillcolor=green,group=6]

        F1->nodo1_1
        {rank=same;F1;nodo1_1}
        F2->nodo2_2
        nodo2_2->nodo2_4
        {rank=same;F2,nodo2_2,nodo2_4}
        F3->nodo3_4
        {rank=same;F3,nodo3_4}
        F4->nodo4_4
        {rank=same;F4,nodo4_4}
        F5->nodo5_3
        nodo5_3->nodo5_5
        {rank=same;F5,nodo5_3,nodo5_5}
        C1->nodo1_1
        C2->nodo2_2
        C4->nodo2_4
        nodo2_4->nodo3_4
        nodo3_4->nodo4_4
        C3->nodo5_3
        C5->nodo5_5
    }
}    
    '''

    miarchivo=open('graphviz.dot','w')
    miarchivo.write(graphviz)
    miarchivo.close()
    system('dot -Tpng graphviz.dot -o graphviz.png')
    system('cd ./graphviz.png')
    startfile('graphviz.png')




generarGraphviz()