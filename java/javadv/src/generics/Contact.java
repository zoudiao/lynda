package generics;

/**
 * Created by eyifang on 2017/10/24.
 */
public class Contact {
    String salutation;
    String fName;
    String lName;
    String phoneNumber;

    public Contact(String salutation,String fName,String lName,String phoneNumber){
        this.salutation = salutation;
        this.fName = fName;
        this.lName = lName;
        this.phoneNumber = phoneNumber;
    }

    public String getSalutation(){
        return salutation;
    }

    public void setSalutation(String salutation){
        this.salutation = salutation;

    }

    public String getfName(){
        return fName;
    }

    public void setfName(String fName){
        this.fName = fName;
    }

    public String getlName(){
        return lName;
    }

    public void setlName(String lName){
        this.lName = lName;
    }

    public String getPhoneNumber(){
        return phoneNumber;
    }

    public void setPhoneNumber(String phoneNumber){
        this.phoneNumber = phoneNumber;
    }

    public String toString(){
        return this.salutation+","+this.fName+","+this.lName+","+this.phoneNumber;
    }
}
