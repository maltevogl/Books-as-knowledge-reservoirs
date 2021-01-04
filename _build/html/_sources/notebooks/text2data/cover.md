# From objects to data

Reading a book gives us information (and fun!) but it is a slow method. If we want to read many books, we need a lot of time at our disposal.

So how can we read many books in a short time and still get out some information?

Entrance _Distant reading_ and Co.  

Distant reading requires as a first step, that the library we are interested in is _machine readable_. Once we have made a picture from every page of a book, we can use OCR to embedd the text in the image. In a second step we can try some automated processes to extract the structure of the text on a page, and save the result in the _TEI_ format.

In the following, we discuss some aspects of availability and biases in these steps and start with some introductory exercises.

## OCR pitfalls and opportunities

  - OCR = Optical character recognition
  - Make sources machine-readable
  - Most common programs good for "modern" (i.e. printed!) texts only (Abby / Teseract)
  - Many other approaches, see e.g. [OCR4all](https://www.uni-wuerzburg.de/en/zpd/ocr4all)
  - Tesseract is Open Source and useful tutorials can be found easily, see e.g. [here](https://medium.com/better-programming/beginners-guide-to-tesseract-ocr-using-python-10ecbb426c3d).

  > For texts spanning a wide period of time, OCR quality will vary a lot

### Example 1

As a first example for data quality, have a look at
Leo Bergmanns _Das Buch der Arbeit_ from 1855. Written in Fraktur, the text is still recognized and readable. However, we can find several errors in the OCR and the text structure is not recognized very well.

[STABI Example](https://digital.staatsbibliothek-berlin.de/werkansicht?PPN=PPN76673319X&PHYSID=PHYS_0011&view=fulltext-parallel&DMDID=DMDLOG_0001)

## Scanning quality

  - OCR quality is improved by higher resolution images
  - But what about file size? ➡️ For 400dpi, one page eq. 40 MB
  - To research paper / materiality of sources, even higher resolution might be necessary

> Long term preservation of raw data raises questions on data quality

### Example 2

- What about other languages?

![Vespucci, B. et al.; Nota eorum quae in hoc libro continentur ... ](assets/OCRexample.png)

Source: [ECHO at MPIWG](http://echo.mpiwg-berlin.mpg.de/ECHOdocuView?url=/permanent/library/0PY87NRF/index.meta&pn=8)

## Existing collections

There are already many existing text collections. Depending on the initial research question, it can be much faster to use them as the starting point.
To capture the full structure of a text, many collections use the Text Encoding Initiative (TEI) standard based on XML. See e.g. [TEI-C](https://tei-c.org/) for an introduction.

  - [LOC](https://crowd.loc.gov/topics/suffrage-women-fight-for-the-vote/): Crowd-sourced transcriptions
  - [Textgrid](https://textgridrep.org/repository.html): German texts in TEI format
  - [Newton Project](http://www.newtonproject.ox.ac.uk/): Works and correspondence of Isaac Newton
  - [Verfassungsschutzberichte](https://verfassungsschutzberichte.de/): All public reports from the _Office for the Protection of the Constitution_
  - [Arxiv](https://arxiv.org): Physics preprints of the last decades

## Exercises

### Exercise 1

  - Use a PDF you are interested in and convert it to TEI using Grobid
    - URL: [GROBID](http://cloud.science-miner.com/grobid/)

  - What result do you get?  
  - Can it be converted, why not?
  - Is the information of authors/publishers correct? Only if you use an academic paper..


### Exercise 2

_Installation of JupyterLab can be done with pip as well..._

  - Download and install [Anaconda](https://www.anaconda.com/products/individual)
  - Open JupyterLab
  - Download material from github
  - Have a look in the folder _Working_with_Jupyter_

### Exercise 3

  - Download material _text2data_
  - Evaluate notebook _Text2Data_1.ipynb_
    - Do you need to install a new package?
  - Try to load a new text resource
    - E.g. from [Textgrid](https://textgrid.de/de/digitale-bibliothek), or a PDF you converted using Grobid.
