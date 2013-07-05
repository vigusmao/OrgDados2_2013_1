public class TrieNode {

    private char valor;
    private TrieNode[] filhos;
    private boolean end;

    public TrieNode() {
        this.filhos = new TrieNode[26];   // implementacao com array (alternativa: lista)
        this.end = false;
    }

    public TrieNode(char valor) {
        this();
        this.valor = valor;
    }

    public boolean isEnd() {
        return end;
    }

    public char getValor() {
        return valor;
    }

    public TrieNode getFilho(char caracter) throws Exception {
        if ((caracter < 'a') || (caracter > 'z')) {
            throw new Exception("caracter = " + caracter);
        }
        TrieNode filho = this.filhos[caracter - 'a'];
        return filho;
    }

    public void adicionarPalavra(String palavra) {
        if (palavra.isEmpty()) {
            this.end = true;    // chegou ao fim da palavra --> no corrente eh final
            return;
        }

        char caracter = palavra.charAt(0);
        TrieNode filho = null;
        try {
            filho = getFilho(caracter);
        } catch (Exception e) {
            System.out.println(e.getMessage());
            e.printStackTrace();
        }
        if (filho == null) {
            filho = new TrieNode(caracter);
            this.filhos[caracter - 'a'] = filho;
        }
        filho.adicionarPalavra(palavra.substring(1));
    }

    public void spillGuts() {
        System.out.print(this.valor);
        if (this.end) {
            System.out.print("(*)");  // (*) indica que o no eh fim de palavra
        };
        System.out.print(": ");

        for(int i = 0; i < this.filhos.length; i++) {
            if (this.filhos[i] != null) {
                System.out.print(this.filhos[i].getValor() + "\t");
            }
        }
        System.out.println();
        for(int i = 0; i < this.filhos.length; i++) {
            if (this.filhos[i] != null) {
               this.filhos[i].spillGuts();
            }
        }
    }
}
