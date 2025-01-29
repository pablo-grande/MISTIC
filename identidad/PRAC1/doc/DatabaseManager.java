import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.security.SecureRandom;
import java.util.Base64;
import java.util.Scanner;
import java.io.FileWriter;
import java.io.FileReader;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.File;
import java.io.UnsupportedEncodingException;
import java.util.Iterator;
import java.util.ArrayList;


public class DatabaseManager {

  private static String pepper = "w3X7ddbbyd3DT0b+Oh1+Dg==";
  private static String databaseFile = "/opt/apache-tomcat-9.0.27/lib/database.txt";
  private static String separator = ":";
  private static int keystretchingIndex = 4;

  private static String bytesToString(byte[] input) {
    return Base64.getEncoder().encodeToString(input);
  }

  private static byte[] StringToBytes(String input) {
    return Base64.getDecoder().decode(input.getBytes());
  }

  public static void main(String[] args)
  throws NoSuchAlgorithmException, FileNotFoundException, IOException {
    String firstName, lastName, username, password = "";
    ArrayList<String> roles = new ArrayList<String>();
    //create users
    roles.add("AC");
    roles.add("GCFP");
    roles.add("GNT");
    roles.add("GCP");
    saveUser("Ender", "Wiggin", "ender", "dragon78", roles);
    roles.clear();

    roles.add("GCFP");
    saveUser("Petra", "Arkanian", "petra", "phoenix8", roles);
    roles.clear();

    roles.add("GNT");
    saveUser("Bonzo", "Madrid", "bonzo", "salamand", roles);
    roles.clear();

    roles.add("GCP");
    saveUser("Carn", "Carby", "carn", "rabbit78", roles);
    roles.clear();

    roles.add("A");
    saveUser("Dink", "Meeker", "dink", "rat45678", roles);
  }

  private static String get_SHA3_512_SecurePassword(String passwordToHash, byte[] salt)
  throws NoSuchAlgorithmException {
    byte[] bytes = null;
    MessageDigest md = MessageDigest.getInstance("SHA3-512");
    for (int i=0; i<keystretchingIndex; i++){
      md.update(salt);
      md.update(StringToBytes(pepper));
      bytes = md.digest(passwordToHash.getBytes());
    }
    StringBuilder sb = new StringBuilder();
    for(int i=0; i<bytes.length ;i++) {
      sb.append(Integer.toString((bytes[i] & 0xff) + 0x100, 16).substring(1));
    }
    return sb.toString();
  }

  private static byte[] salt() throws NoSuchAlgorithmException {
    SecureRandom sr = SecureRandom.getInstance("SHA1PRNG");
    byte[] salt = new byte[16];
    sr.nextBytes(salt);
    return salt;
  }

  /**
  1. Hash password
  2. Write into password file 'username';'hashed password:salt'
  */
  private static void saveUser(String firstName, String lastName, String username, String password, ArrayList<String> roles)
  throws NoSuchAlgorithmException, FileNotFoundException, IOException {
    byte[] salt = salt();
    String securePassword = get_SHA3_512_SecurePassword(password, salt);
    String roleLine = "";
    for (String role : roles){
      roleLine = roleLine.concat(role).concat(separator);
    }
    String writeLine = firstName.concat(separator).concat(lastName).concat(separator)
    .concat(username).concat(separator).concat(securePassword).concat(separator)
    .concat(bytesToString(salt)).concat(separator).concat(roleLine).concat("\n");

    //write data into file. true = appending
    FileWriter fw = new FileWriter(databaseFile, true);
    fw.write(writeLine);
    fw.close();
  }

  /**
  1. Find password and salt of user by username param in password file
  2. Create hash password from param and salt
  3. Compare hashes from file and from params
  */
  public static ArrayList<String> getUserData(String username, String password)
  throws NoSuchAlgorithmException, FileNotFoundException, IOException {
    String retrievedPassword = "";
    String retrievedSalt = "";
    ArrayList<String> userdata = new ArrayList<String>();

    Scanner sc = new Scanner(new FileReader(databaseFile));
    while (sc.hasNextLine()){
      String line = sc.nextLine();
      String[] dbData = line.split(separator);
      if (dbData[2].equals(username)) {
        retrievedPassword = dbData[3];
        retrievedSalt = dbData[4];
        if (get_SHA3_512_SecurePassword(password, StringToBytes(retrievedSalt))
        .equals(retrievedPassword)){
          userdata.add(dbData[0]);
          userdata.add(dbData[1]);
          userdata.add(dbData[2]);
          userdata.add(dbData[3]);
          userdata.add(dbData[4]);
          for (int i=5; i<dbData.length; i++){
            userdata.add(dbData[i]);
          }
        }
      }
    }
    return userdata;
  }

}
