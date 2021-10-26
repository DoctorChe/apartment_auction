import axios from "axios";

const API_URL = "http://localhost:8082/auth/";

class AuthService {
  login(user) {
    return axios
      .post(API_URL + "sign-in", {
        username: user.username,
        // password: user.password,
      })
      .then((response) => {
        // if (response.data.accessToken) {
        //   localStorage.setItem("user", JSON.stringify(response.data));
        // }
        console.log(response.data);

        return response.data;
      });
  }

  logout() {
    localStorage.removeItem("user");
  }

  //   register(user) {
  //     return axios.post(API_URL + "signup", {
  //       username: user.username,
  //       email: user.email,
  //       password: user.password,
  //     });
  //   }
}

export default new AuthService();
