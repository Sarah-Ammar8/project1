
package javaapplication35;

public class Library {
    private int LibraryID;
    private String LibrarianName;
    private String BookSection;
    private int TotalBooks;

    public Library(int LibraryID, String LibrarianName, String BookSection, int TotalBooks) {
        this.LibraryID = LibraryID;
        this.LibrarianName = LibrarianName;
        this.BookSection = BookSection;
        this.TotalBooks = TotalBooks;
    }
    
    public void LibraryDetails(){
        System.out.println("Library ID: "+LibraryID);
        System.out.println("Librarian Name: "+LibrarianName);
        System.out.println("Book Section: "+BookSection);
        System.out.println("Total Books: "+TotalBooks);
        System.out.println("------------------------------------");
    }
    
    public void SearchBooks(){
        System.out.println("Searching for books...");
    }
    
    public void LendBooks(){
        System.out.println("Lending book...");
    }
    
    public void ReturnBooks(){
        System.out.println("Returning book...");
    }
    
    public void PayFine(){
        System.out.println("Paying fine...");
    }

    public int getLibraryID() {
        return LibraryID;
    }

    public void setLibraryID(int LibraryID) {
        this.LibraryID = LibraryID;
    }

    public String getLibrarianName() {
        return LibrarianName;
    }

    public void setLibrarianName(String LibrarianName) {
        this.LibrarianName = LibrarianName;
    }

    public String getBookSection() {
        return BookSection;
    }

    public void setBookSection(String BookSection) {
        this.BookSection = BookSection;
    }

    public int getTotalBooks() {
        return TotalBooks;
    }

    public void setTotalBooks(int TotalBooks) {
        this.TotalBooks = TotalBooks;
    }
    
    
}
