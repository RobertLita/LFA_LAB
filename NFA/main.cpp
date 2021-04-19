#include <iostream>
#include <fstream>
#include <vector>
#include <cstring>
using namespace std;
ifstream f("nfa_in.txt");
ofstream g("nfa_out.txt");
/*
Nod = Stare, mi-am adus aminte ulterior denumirea corecta dar era prea mult de modificat :D
-Voi retine tranzitiile intr-o structura de tipul stare1 stare2 caracter

-Voi retine pentru fiecare stare tranzitiile care pleaca din respectiva stare si daca este final sau nu

-Pentru fiecare stare, incepand cu cea initiala, pun la finalul unui vector toate starile in care se ajunge cu litera
curenta si vad daca in final se termina cuvantul.
-Campurile din structura drum ajuta sa reconstitui traseul dupa ce un cuvant este acceptat si pt fiecare pozitie
din vector sa retinem starea din el si litera pozitia in cuvant la care s-a ajuns pana atunci.

*/
struct Tranzitie
{
    short int x,y;
    char c;
};
struct Nod
{
    bool eFinal;
    vector<Tranzitie> tranzitii;
};
struct drum
{
    short int nod_curent,poz_ant,poz_litera;
};

Nod noduri[100];
vector <drum> D;

void refa_traseu(int poz)
{
    if(poz!=-1)
    {
        refa_traseu(D[poz].poz_ant);
        g<<D[poz].nod_curent<<' ';
    }
}
bool eAcceptat(char *cuvant,short int nod_init)
{
    int p=0;
    drum drum_curent;
    drum_curent.nod_curent=nod_init;
    drum_curent.poz_ant=-1;
    drum_curent.poz_litera=0;
    D.push_back(drum_curent);
    while(p<D.size())
    {
        for(auto tranzitie:noduri[D[p].nod_curent].tranzitii)
            if(tranzitie.c==cuvant[D[p].poz_litera])
            {
                drum_curent.poz_ant=p;
                drum_curent.nod_curent=tranzitie.y;
                drum_curent.poz_litera=D[p].poz_litera+1;
                if(drum_curent.poz_litera==strlen(cuvant) && noduri[drum_curent.nod_curent].eFinal==1)
                {
                    D.push_back(drum_curent);
                    return 1;
                }
                if(drum_curent.poz_litera<strlen(cuvant))
                    D.push_back(drum_curent);
            }
        p++;
    }
    return 0;
}
int main()
{
    short int n_noduri,n_tranzitii,n_finale,nod_init,n_cuvinte;
    f>>n_noduri>>n_tranzitii;
    for(int i=1; i<=n_tranzitii; i++)
    {
        short int tranzitie_x,tranzitie_y;
        char tranzitie_caracter;
        f>>tranzitie_x>>tranzitie_y>>tranzitie_caracter;
        Tranzitie T;
        T.x=tranzitie_x;
        T.y=tranzitie_y;
        T.c=tranzitie_caracter;
        noduri[T.x].tranzitii.push_back(T);
    }
    f>>nod_init>>n_finale;
    for(int i=0; i<n_finale; i++)
    {
        short int nod;
        f>>nod;
        noduri[nod].eFinal=1;
    }
    f>>n_cuvinte;
    for(int i=0; i<n_cuvinte; i++)
    {
        char cuvant[200];
        f>>cuvant;
        if(eAcceptat(cuvant,nod_init))
        {
            g<<"DA\n"<<"Traseu: ";
            refa_traseu(D.size()-1);
            g<<'\n';
        }
        else
        {
            g<<"NU\n";
        }
    }
    return 0;
}
