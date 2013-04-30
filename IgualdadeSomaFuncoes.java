import java.util.ArrayList;
import java.util.HashMap;
import java.util.Random;

/**
 * Created with IntelliJ IDEA.
 * User: vigusmao
 * Date: 4/30/13
 * Time: 2:22 PM
 * To change this template use File | Settings | File Templates.
 */
public class IgualdadeSomaFuncoes {

    private static int TAMANHO_HASH = 100000;
    private static int IMAGEM_F = 1000;

    public static int N = 5000;

    private static HashMap<Integer,Integer> tabela_f;

    static void popula_f() {
        for (int i = 1; i <= TAMANHO_HASH; i++) {
           tabela_f.put(i, new Long(Math.round((-1 + Math.random() * 2) * IMAGEM_F)).intValue());
        }
    }

    public static int f(int x) {
        return tabela_f.get(x);
    }

    private static class Tripla {
        int a, b, c;
        Tripla(int a, int b, int c) {
            this.a = a;
            this.b = b;
            this.c = c;
        }
    }



    public static void main(String[] args) {

        popula_f();

        HashMap<Integer, ArrayList<Tripla>> mapa = new HashMap<Integer, ArrayList<Tripla>>();

        // O(N^3)
        for (int a = 1; a <= N; a++) {
            for (int b = a; b <= N; b++) {
                for (int c = b; c <= N; c++) {
                    int r = f(a) + f(b) + f(c);
                    ArrayList<Tripla> lista = mapa.get(r);
                    if (lista == null) {
                        lista = new ArrayList<Tripla>();
                    }
                    lista.add(new Tripla(a, b, c));
                    mapa.put(r, lista);
                }
            }
        }
    }
}
