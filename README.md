# Smart Bookmark API
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/iamyajat/Smart-Bookmark-API">
    <img src="https://images.unsplash.com/photo-1506445007064-9dda1f11b5b6?ixlib=rb-1.2.1&q=80&fm=jpg&crop=entropy&cs=tinysrgb&dl=victoria-bilsborough-b9zbVD--6I0-unsplash.jpg&w=2400" alt="Photo by Victoria Bilsborough" width="640" height="426">
  </a>
 
  <h3 align="center">SMART BOOKMARK API</h3>

  <p align="center">
    An API that can classify websites into 10 different categories
    <br />
    <a href="https://github.com/iamyajat/Smart-Bookmark-API/blob/master/README.md"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/iamyajat/smart-bookmark-api">Demo (Coming Soon)</a>
    ·
    <a href="https://github.com/iamyajat/smart-bookmark-api/issues">Report Bug</a>
    ·
    <a href="https://github.com/iamyajat/smart-bookmark-api/issues">Request Feature</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

An API that can classify a given url into various different categories.

#### Categories
- Sports
- News
- Fitness & Wellbeing
- Food and Recipes
- Politics
- Entertainment
- Business
- Blogs
- Science & Technology
- NSFW


### Built With

* [Python 3.8.9](https://www.python.org/downloads/release/python-389/)
* [FastAPI](https://fastapi.tiangolo.com/)
* [TensorFlow 2](https://www.tensorflow.org/)



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites
- Python 3.8.9 and the latest version of pip.
- Download the weights for the model from [here](https://www.dropbox.com/s/faqqelakxy1move/weights3.h5?dl=0) and put them in as [./assets/weights/weights3.h5](https://github.com/iamyajat/smart-bookmark-api/tree/master/assets/weights)
### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/iamyajat/smart-bookmark-api.git
   ```
2. Install `virtualenv`
   ```sh
   pip install virtualenv
   ```
3. Create a virtual environment
   ```sh
   python -m venv env
   ```
   ```sh
   env\Scripts\activate
   ```
4. Install all requirements
   ```sh
   pip install -r requirements.txt
   ```
5. Start the API
   ```sh
   uvicorn main:app --reload
   ```

<!-- USAGE EXAMPLES -->
## Usage

To try the API out, go to [https://127.0.0.1/docs#/](https://127.0.0.1/docs#/) and test the different end-points out.



<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/iamyajat/smart-bookmark-api/issues) for a list of proposed features (and known issues).



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'feat: AmazingFeature'`)
   - Please refer to the commit guidelines mentioned [here](https://www.conventionalcommits.org/en/v1.0.0/).
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

<a href="https://www.iamyajat.co/" target="_blank"><img alt="Github" src="https://img.shields.io/badge/-Website-brightgreen?style=for-the-badge&logo=appveyor&logoColor=white&color=999900&logo=data:null" /></a>
<a href="https://linkedin.com/in/iamyajat" target="_blank"><img alt="LinkedIn" src="https://img.shields.io/badge/linkedin-%230077B5.svg?&style=for-the-badge&logo=linkedin&logoColor=white" /></a>
<a href="https://twitter.com/iamyajat" target="_blank"><img alt="Twitter" src="https://img.shields.io/badge/twitter-%231DA1F2.svg?&style=for-the-badge&logo=twitter&logoColor=white" /></a>
<a href="https://instagram.com/iamyajat" target="_blank"><img alt="Instagram" src="https://img.shields.io/badge/instagram-%FF69B4.svg?&style=for-the-badge&logo=instagram&logoColor=white&color=cd486b" /></a>


Project Link: [https://github.com/iamyajat/smart-bookmark-api](https://github.com/iamyajat/smart-bookmark-api)




<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/iamyajat/Smart-Bookmark-API.svg?style=for-the-badge
[contributors-url]: https://github.com/iamyajat/smart-bookmark-api/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/iamyajat/Smart-Bookmark-API.svg?style=for-the-badge
[forks-url]: https://github.com/iamyajat/smart-bookmark-api/network/members
[stars-shield]: https://img.shields.io/github/stars/iamyajat/Smart-Bookmark-API.svg?style=for-the-badge
[stars-url]: https://github.com/iamyajat/smart-bookmark-api/stargazers
[issues-shield]: https://img.shields.io/github/issues/iamyajat/Smart-Bookmark-API.svg?style=for-the-badge
[issues-url]: https://github.com/iamyajat/smart-bookmark-api/issues
[license-shield]: https://img.shields.io/github/license/iamyajat/Smart-Bookmark-API.svg?style=for-the-badge
[license-url]: https://github.com/iamyajat/Smart-Bookmark-API/blob/master/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/iamyajat
