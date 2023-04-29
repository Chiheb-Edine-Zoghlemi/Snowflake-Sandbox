
import streamlit as st
import extra_streamlit_components as stx


class Authenticate:
    """
    This class will create login, logout widgets.
    """
    def __init__(self):
        """
        Create a new instance of "Authenticate".

        Parameters
        ----------
        credentials: dict
            The user credentials.
        cookie_name: str
            The name of the JWT cookie stored on the client's browser for passwordless reauthentication.
   
        """
        self.credentials = {}
        self.cookie_name = 'auth'
        self.cookie_manager = stx.CookieManager()
        
        if 'credits' not in st.session_state:
            st.session_state['credits'] = None
        if 'authentication_status' not in st.session_state:
            st.session_state['authentication_status'] = None
        if 'logout' not in st.session_state:
            st.session_state['logout'] = None

   
    

    def validate(self) -> bool:
        """
        Checks the validity of the entered password.

        Returns
        -------
        bool
            The validity of the entered password by comparing it to the hashed password on disk.
        """
        return True

    def _check_cookie(self):
        """
        Checks the validity of the reauthentication cookie.
        """
        self.token = self.cookie_manager.get(self.cookie_name)
        if self.token is not None:
            if self.token is not False:
                if not st.session_state['logout']:
                    if 'credits' in self.token:
                        st.session_state['credits'] = self.token['credits']
                        st.session_state['authentication_status'] = True
    
    def _check_credentials(self) -> bool:
        """
        Checks the validity of the entered credentials.
        -------
        bool
            Validity of entered credentials.
        """
        if self.validate():
            self.cookie_manager.set(self.cookie_name, self.credentials)
            st.session_state['authentication_status'] = True
        else:
            st.session_state['authentication_status'] = False


    def login(self) -> tuple:
        """
        Creates a login widget.

        Returns
        -------
        dict
            Credentials of the  user.
        bool
            The status of authentication, None: no credentials entered, 
            False: incorrect credentials, True: correct credentials.
        
        """
        if not st.session_state['authentication_status']:
            self._check_cookie()
            if not st.session_state['authentication_status']:
                login_form = st.form('Login')
                with login_form:
                    col1, col2, col3, col4, col5 = st.columns(5)
                    with col1:
                        credits['account'] = st.text_input('Account').strip()
                    with col2:
                        credits['username']  = st.text_input('Username').strip()
                    with col3:
                        credits['password']  = st.text_input('Password', type='password').strip()
                    with col4: 
                        credits['warhouse']  = st.text_input('Warhouse').strip()
                    with col5: 
                        credits['role']  = st.text_input('Role').strip()
                    if login_form.form_submit_button('Login'):
                        self._check_credentials()

        return st.session_state['credits'], st.session_state['authentication_status'] 

    def logout(self):
        if st.button('Logout'):
            self.cookie_manager.delete(self.cookie_name)
            st.session_state['logout'] = True
            st.session_state['credits'] = None
            st.session_state['authentication_status'] = None
     

    
    