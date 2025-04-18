
package javaapplication35;

public class Canteen {
    private int Inchargeld;
    private String[] ItemsList;

    public Canteen(int Inchargeld, String[] ItemsList) {
        this.Inchargeld = Inchargeld;
        this.ItemsList = ItemsList;
    }
    
    public void ShowItems(){
        System.out.println("Available items in the canteen: ");
        for (String item:ItemsList){
            System.out.println(item);
        }
    }
    
    public void Buy(){
        System.out.println("Buying item...");
    }

    public int getInchargeld() {
        return Inchargeld;
    }

    public void setInchargeld(int Inchargeld) {
        this.Inchargeld = Inchargeld;
    }

    public String[] getItemsList() {
        return ItemsList;
    }

    public void setItemsList(String[] ItemsList) {
        this.ItemsList = ItemsList;
    }
    
}
