# HypeLinks API
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/iamyajat/hypelinks-API">
    <img src="https://images.unsplash.com/photo-1506445007064-9dda1f11b5b6?ixlib=rb-1.2.1&q=80&fm=jpg&crop=entropy&cs=tinysrgb&dl=victoria-bilsborough-b9zbVD--6I0-unsplash.jpg&w=2400" alt="Photo by Victoria Bilsborough" width="640" height="426">
  </a>
 
  <h3 align="center">HYPELINKS API</h3>

  <p align="center">
    A Smart Bookmark API that can classify websites into 10 different categories
    <br />
    <a href="https://github.com/iamyajat/hypelinks-API/blob/master/README.md"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://hypelinks-api.iamyajat.com/docs">Demo</a>
    ·
    <a href="https://github.com/iamyajat/hypelinks-api/issues">Report Bug</a>
    ·
    <a href="https://github.com/iamyajat/hypelinks-api/issues">Request Feature</a>
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
- Food & Recipes
- Politics
- Entertainment
- Business
- Blogs
- Science & Technology
- NSFW


### Built With

* [Python 3.8.10](https://www.python.org/downloads/release/python-3810/)
* [FastAPI](https://fastapi.tiangolo.com/)
* [TensorFlow 2](https://www.tensorflow.org/)



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites
- Python 3.8.10 and the latest version of pip.


### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/iamyajat/hypelinks-api.git
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
   .\env\Scripts\activate
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

To try the API out, go to [http://127.0.0.1:8000/docs/](http://127.0.0.1:8000/docs/) and test the different end-points out.



<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/iamyajat/hypelinks-api/issues) for a list of proposed features (and known issues).



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'feat: AmazingFeature'`)
   - Please refer to the commit guidelines mentioned [here](https://www.conventionalcommits.org/en/v1.0.0/).
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Contributors

<table>
<tr>
    <td align="center" style="word-wrap: break-word; width: 150.0; height: 150.0">
        <a href=https://github.com/iamyajat>
            <img src=https://avatars.githubusercontent.com/u/68477362?v=4 width="100;"  style="border-radius:50%;align-items:center;justify-content:center;overflow:hidden;padding-top:10px" alt=Yajat Malhotra/>
            <br />
            <sub style="font-size:14px"><b>Yajat Malhotra</b></sub>
        </a>
    </td>
    <td align="center" style="word-wrap: break-word; width: 150.0; height: 150.0">
        <a href=https://github.com/PAARTH2608>
            <img src=https://avatars.githubusercontent.com/u/76266935?v=4 width="100;"  style="border-radius:50%;align-items:center;justify-content:center;overflow:hidden;padding-top:10px" alt=PAARTH2608/>
            <br />
            <sub style="font-size:14px"><b>PAARTH2608</b></sub>
        </a>
    </td>
    <td align="center" style="word-wrap: break-word; width: 150.0; height: 150.0">
        <a href=https://github.com/programmerraja>
            <img src=https://avatars.githubusercontent.com/u/44333589?v=4 width="100;"  style="border-radius:50%;align-items:center;justify-content:center;overflow:hidden;padding-top:10px" alt=K.Boopathi/>
            <br />
            <sub style="font-size:14px"><b>K.Boopathi</b></sub>
        </a>
    </td>
</tr>
</table>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

<a href="https://www.iamyajat.co/" target="_blank"><img alt="Github" src="https://img.shields.io/badge/-Website-brightgreen?style=for-the-badge&logo=appveyor&logoColor=white&color=999900&logo=data:null" /></a>
<a href="https://linkedin.com/in/iamyajat" target="_blank"><img alt="LinkedIn" src="https://img.shields.io/badge/linkedin-%230077B5.svg?&style=for-the-badge&logo=linkedin&logoColor=white" /></a>
<a href="https://twitter.com/iamyajat" target="_blank"><img alt="Twitter" src="https://img.shields.io/badge/twitter-%231DA1F2.svg?&style=for-the-badge&logo=twitter&logoColor=white" /></a>
<a href="https://instagram.com/iamyajat" target="_blank"><img alt="Instagram" src="https://img.shields.io/badge/instagram-%FF69B4.svg?&style=for-the-badge&logo=instagram&logoColor=white&color=cd486b" /></a>


Project Link: [https://github.com/iamyajat/hypelinks-api](https://github.com/iamyajat/hypelinks-api)




<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/iamyajat/hypelinks-API.svg?style=for-the-badge
[contributors-url]: https://github.com/iamyajat/hypelinks-api/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/iamyajat/hypelinks-API.svg?style=for-the-badge
[forks-url]: https://github.com/iamyajat/hypelinks-api/network/members
[stars-shield]: https://img.shields.io/github/stars/iamyajat/hypelinks-API.svg?style=for-the-badge
[stars-url]: https://github.com/iamyajat/hypelinks-api/stargazers
[issues-shield]: https://img.shields.io/github/issues/iamyajat/hypelinks-API.svg?style=for-the-badge
[issues-url]: https://github.com/iamyajat/hypelinks-api/issues
[license-shield]: https://img.shields.io/github/license/iamyajat/hypelinks-API.svg?style=for-the-badge
[license-url]: https://github.com/iamyajat/hypelinks-API/blob/master/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/iamyajat
