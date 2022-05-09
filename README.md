# Argy-markets

<div id="top"></div>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/pjr95/argy-markets>
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">ARGY-MARKETS</h3>

  <p align="center">
    A repo with tools, screeners and scripts useful for the Argentinan capital markets.
    <br />
    <a href="https://github.com/pjr95/argy-markets"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/pjr95/argy-markets">View Demo</a>
    ·
    <a href="https://github.com/pjr95/argy-markets/issues">Report Bug</a>
    ·
    <a href="https://github.com/pjr95/argy-markets/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
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
        <li><a href="#technical-prerequisites">Technical Prerequisites</a></li>
        <li><a href="#market-prerequisites">Market Prerequisites</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

This repo was created to organise and deploy several tools and utilities for the analysis of the Argentinian capital markets. 

The turbulent financial markets in Argentina require a set of utensils that can ensure greater deep of analysis than the one than a simple spreadsheet could provide.

In this repo you would find:
* Screeners and monitors, using different assets, connections or metrics.
* Functions that will allow you to analyse a diverse set of asset classes.
* Utilities and scripts for creating your own monitors, screeners and asset related tools!

I'll adding more content in the future, including more screeners, asset classes modules, back office utilities, educational content, and more! Feel free to contribute, open an issue or contacting me for new ideas. **WAGMI** guys!


<p align="right">(<a href="#top">back to top</a>)</p>



### Built With

This section should list any major frameworks/libraries used to bootstrap your project. Leave any add-ons/plugins for the acknowledgements section. Here are a few examples.

* [Python](https://www.python.org/)
* [R](https://www.r-project.org/)
* [Microsoft Excel](https://www.microsoft.com/es-ar/microsoft-365/excel)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

This part is tricky, as we have a series of screeners and scripts using various sources. Hence, we will cover only the technical prerequisites here.

### Technical prerequisites

First of all you need to have installed [Python](https://www.python.org/downloads/) version for most of the scripts and [R](https://cran.r-project.org/mirrors.html) for some others. The instructions for the installation of either are contained on the websites.

To check if you have Python installed you could run the command (on both Unix and Windows systems) on the terminal/command line:

```
python --version
```

alternatively:

```
python3 --version
```

Though you should use an updated python version, 3.10.X will suffice.

Once you have checked your version, and updated/install it if necessary, you will need to use a package manager, such as [conda](https://anaconda.org/anaconda/conda#:~:text=Description%20Conda%20is%20an%20open%20source%20package%20management,programs%20but%20can%20package%20and%20distribute%20any%20software.?msclkid=13839272cf2511ec84ed0b86325382cf) or [pip](https://pypi.org/project/pip/?msclkid=a92d23d8cf2611ecb37b18975da6abee) to manage the libraries and environments that you will be using.

Pipenv was used to create this repo and the Pipfile.lock and Pipfile are available in the repo.

If you wish to use pipenv, you need to install it first throughout pip or conda. The pip way will be used to illustrate the whole process:

```
pip install pipenv
```

alternatively:

```
pip3 install pipenv
```
After successful installation, you should run the following command in the repo directory:

```
pipenv shell
```

This will create a virtual environment, where the dependencies are going to be installed. 

As you have the Pipfile.lock, you should run the following command to install all the necessary dependencies:

```
pipenv install --ignore-pipfile
```
And with this, you are ready to go!

### Market prerequisites

Altought the technical requirements for running the scripts are set to this point, you will still need some API keys, accounts in brokers, and/or external programmes to run some of the screeners and monitors.

Each kind of monitor is has its own readme.md (to date iol and multi screeners), so you should check what is needed inside the proper folder.

<p align="right">(<a href="#top">back to top</a>)</p>




<!-- ROADMAP -->
## Roadmap


- [ ] Add Additional Templates w/ Examples
- [ ] Add Changelog
- [ ] Multi-language Support: Spanish


See the [open issues](https://github.com/pjr95/argy-markets/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions not only are greatly appreciated but highly necessary. As an open source project, the intent of this is to serve as a repository (no pun intended) to diverse utilities and tools relevant for traders, quant researchers, scholars, and anyone who might find it useful.

If you have a suggestion that would improve this repo, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star and thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the GNU General Public License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Pablo José Romero - [@your_twitter](https://twitter.com/your_username) - email@example.com

Project Link: [https://github.com/your_username/repo_name](https://github.com/your_username/repo_name)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

Use this space to list resources you find helpful and would like to give credit to. I've included a few of my favourites to kick things off!

* [Choose an Open Source License](https://choosealicense.com)
* [GitHub Emoji Cheat Sheet](https://www.webpagefx.com/tools/emoji-cheat-sheet)
* [Malven's Flexbox Cheatsheet](https://flexbox.malven.co/)
* [Malven's Grid Cheatsheet](https://grid.malven.co/)
* [Img Shields](https://shields.io)
* [GitHub Pages](https://pages.github.com)
* [Font Awesome](https://fontawesome.com)
* [React Icons](https://react-icons.github.io/react-icons/search)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/pjr95/argy-markets.svg?style=for-the-badge
[contributors-url]: https://github.com/pjr95/argy-markets/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/pjr95/argy-markets.svg?style=for-the-badge
[forks-url]: https://github.com/pjr95/argy-markets/network/members
[stars-shield]: https://img.shields.io/github/stars/pjr95/argy-markets.svg?style=for-the-badge
[stars-url]: hhttps://github.com/pjr95/argy-markets/stargazers
[issues-shield]: https://img.shields.io/github/issues/pjr95/argy-markets.svg?style=for-the-badge
[issues-url]: https://github.com/pjr95/argy-markets/issues
[license-shield]: https://img.shields.io/github/license/pjr95/argy-markets.svg?style=for-the-badge
[license-url]: https://github.com/pjr95/argy-markets/blob/main/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/pjr95/
[product-screenshot]: images/screenshot.png