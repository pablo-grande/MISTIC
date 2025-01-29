import java.util.ArrayList;
import java.security.Principal;
 
public class PlainUserPrincipal implements Principal {
 
    String UserName;
    String FirstName;
    String LastName;
    ArrayList<String> UserRoles;
     
    public PlainUserPrincipal(String name, String firstName, String lastName, ArrayList<String> roles) {
        UserName = name;
        FirstName = firstName;
        LastName = lastName;
        UserRoles = roles;
    }

    public String getName() {
        return UserName;
    }
     
    public String toString() {
        String roles = "";
        for (int i=0; i<UserRoles.size(); i++) {
            roles += UserRoles.get(i);
            if (i<UserRoles.size()-1){
                roles += ", ";
            }
        }
        return (FirstName + " " + LastName + " [" + UserName + "] " + "(" + roles +")");
    }  
 
    public boolean equals(Object obj) {
        if (this == obj) {
            return true;
        }  
        if (obj instanceof PlainUserPrincipal) {
            PlainUserPrincipal other = (PlainUserPrincipal) obj;
            return UserName.equals(other.UserName);
        }  
        return false;
    }  
 
    public int hashCode() {
        return UserName.hashCode();
    }  
}
