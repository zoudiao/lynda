package generics;

/**
 * Created by eyifang on 2017/10/24.
 */
public class Employee {

    String fName;
    String lName;
    String employeeId;

    public Employee(String fName,String lName, String employeeId){
        this.fName = fName;
        this.lName = lName;
        this.employeeId = employeeId;
    }

    public String getfName(){
        return fName;
    }

    public void setfName(String fName){
        this.fName = fName;
    }

    public String toString(){
        return this.fName+","+this.lName+","+this.employeeId;
    }
}
