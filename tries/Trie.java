public class Trie {

    private TrieNode raiz;

    public Trie() {
        raiz = new TrieNode();
    }

    public void adicionarPalavra(String palavra) {
        raiz.adicionarPalavra(palavra);
    }

    public boolean consultarPrefixo(String prefixo)    {
        return consultarPrefixo(prefixo, false);
    }

    public boolean consultarPrefixo(String prefixo, boolean palavraCompleta)    {

        TrieNode noCorrente = this.raiz;
        for(int i = 0; i < prefixo.length(); i++) {
            char proximoCaracter = prefixo.charAt(i);
            try {
                noCorrente = noCorrente.getFilho(proximoCaracter);
            } catch (Exception e) {
                System.out.println(e.getMessage());
                e.printStackTrace();
            }
            if(noCorrente == null) {
                return false;
            }
        }
        return !palavraCompleta || noCorrente.isEnd();
    }

    public void print() {
        this.raiz.spillGuts();
    }



}
