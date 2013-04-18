/**
 * Created with IntelliJ IDEA.
 * User: vigusmao
 * Date: 4/16/13
 * Time: 2:36 PM
 * To change this template use File | Settings | File Templates.
 */
public class TesteStringBuffer {

    public static void main (String[] args) {

        StringBuffer buffer;
        String string;
        long inicio, fim;
        int tamanho;

        for (tamanho = 10000; tamanho <= 100000; tamanho *= 2) {
            System.out.print("\nTamanho = " + tamanho);
            string = "";
            inicio = System.currentTimeMillis();
            for (int i = 0; i < tamanho; i++) {
                string += "a";
            }
            fim = System.currentTimeMillis();
            System.out.print("  --->  tempo (String) = " + (fim - inicio));
        }

        System.out.println();

        for (tamanho = 5000; tamanho <= 10000000; tamanho *= 2) {
            System.out.print("\nTamanho = " + tamanho);
            buffer = new StringBuffer();
            inicio = System.currentTimeMillis();
            for (int i = 0; i < tamanho; i++) {
                buffer.append("a");
            }
            fim = System.currentTimeMillis();
            System.out.print("  --->  tempo (StringBuffer) = " + (fim - inicio));
        }
    }
}
