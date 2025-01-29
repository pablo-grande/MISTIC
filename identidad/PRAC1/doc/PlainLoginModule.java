import java.io.IOException;
import java.util.Map;
import java.util.ArrayList;
import javax.security.auth.Subject;
import javax.security.auth.callback.Callback;
import javax.security.auth.callback.CallbackHandler;
import javax.security.auth.callback.NameCallback;
import javax.security.auth.callback.PasswordCallback;
import javax.security.auth.callback.UnsupportedCallbackException;
import javax.security.auth.login.LoginException;
import javax.security.auth.spi.LoginModule;
import java.security.NoSuchAlgorithmException;


/**
 * Login module that simply matches name and password to perform authentication.
 * If successful, set principal to name and credential to "admin".
 *
 * @author Nicolas Fränkel
 * @since 2 avr. 2009
 */
public class PlainLoginModule implements LoginModule {

    /** Callback handler to store between initialization and authentication. */
    private CallbackHandler handler;

    /** Subject to store. */
    private Subject subject;

    /** Login name. */
    private String login;

    private String firstName;

    private String lastName;

    private ArrayList<String> roles;

    /**
     * This implementation always return false.
     *
     * @see javax.security.auth.spi.LoginModule#abort()
     */
    @Override
    public boolean abort() throws LoginException {

        return false;
    }

    /**
     * This is where, should the entire authentication process succeeds,
     * principal would be set.
     *
     * @see javax.security.auth.spi.LoginModule#commit()
     */
    @Override
    public boolean commit() throws LoginException {

        try {

            PlainUserPrincipal user = new PlainUserPrincipal(login, firstName, lastName, roles);
            PlainRolePrincipal tomcat = new PlainRolePrincipal("tomcat");
            subject.getPrincipals().add(tomcat);
            for (int i=0; i<roles.size(); i++) {
                PlainRolePrincipal role = new PlainRolePrincipal(roles.get(i));
                subject.getPrincipals().add(role);
            }

            subject.getPrincipals().add(user);

            return true;

        } catch (Exception e) {

            throw new LoginException(e.getMessage());
        }
    }

    /**
     * This implementation ignores both state and options.
     *
     * @see javax.security.auth.spi.LoginModule#initialize(javax.security.auth.Subject,
     *      javax.security.auth.callback.CallbackHandler, java.util.Map,
     *      java.util.Map)
     */
    @Override
    public void initialize(Subject aSubject, CallbackHandler aCallbackHandler, Map aSharedState, Map aOptions) {

        handler = aCallbackHandler;
        subject = aSubject;
    }

    /**
     * This method checks whether the name and the password are the same.
     *
     * @see javax.security.auth.spi.LoginModule#login()
     */
    @Override
    public boolean login() throws LoginException {

        Callback[] callbacks = new Callback[2];
        callbacks[0] = new NameCallback("login");
        callbacks[1] = new PasswordCallback("password", true);

        DatabaseManager db = new DatabaseManager();
        ArrayList<String> userData = new ArrayList<String>();

        try {

            handler.handle(callbacks);

            String name = ((NameCallback) callbacks[0]).getName();
            String password = String.valueOf(((PasswordCallback) callbacks[1]).getPassword());

            userData = db.getUserData(name, password);

            if (userData.isEmpty()){

                throw new LoginException("Authentication failed");

            }

            firstName = userData.get(0);
            lastName = userData.get(1);
            login = userData.get(2);

            ArrayList<String> userDataRoles = new ArrayList<String>();

            for (int i=5; i<userData.size(); i++) {
              userDataRoles.add(userData.get(i));
            }

            roles = userDataRoles;

            return true;

        } catch (IOException e) {

            throw new LoginException(e.getMessage());

        } catch (UnsupportedCallbackException e) {

            throw new LoginException(e.getMessage());

        } catch (NoSuchAlgorithmException e) {

            throw new LoginException(e.getMessage());

        }
    }

    /**
     * Clears subject from principal and credentials.
     *
     * @see javax.security.auth.spi.LoginModule#logout()
     */
    @Override
    public boolean logout() throws LoginException {

        try {

            PlainUserPrincipal user = new PlainUserPrincipal(login, firstName, lastName, roles);
            PlainRolePrincipal tomcat = new PlainRolePrincipal("tomcat");

            for (int i=0; i<roles.size(); i++) {
                PlainRolePrincipal role = new PlainRolePrincipal(roles.get(i));
                subject.getPrincipals().remove(role);
            }
            subject.getPrincipals().remove(user);
            subject.getPrincipals().remove(tomcat);

            return true;

        } catch (Exception e) {

            throw new LoginException(e.getMessage());
        }
    }
}
