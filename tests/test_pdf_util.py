
import os

from pdf_trio import pdf_util


def test_extract_pdf_text():

    test_pdf_path = 'tests/files/research/fea48178ffac3a42035ed27d6e2b897cb570cf13.pdf'
    text = pdf_util.extract_pdf_text(test_pdf_path)

    assert text
    assert "Yoshiyuki" in text


def test_extract_pdf_image():

    test_pdf_path = 'tests/files/research/submission_363.pdf'
    img_path = pdf_util.extract_pdf_image(test_pdf_path)
    assert img_path
    img_path = pdf_util.extract_pdf_image(test_pdf_path, page=2)
    assert img_path

    assert test_pdf_path in img_path
    assert img_path.endswith('.jpg')
    os.unlink(img_path)


def test_extract_pdf_prev():
    """
    Guess these are old/unused functions?
    """

    test_pdf_path = 'tests/files/research/fea48178ffac3a42035ed27d6e2b897cb570cf13.pdf'
    text = pdf_util.extract_pdf_text_prev(test_pdf_path)

    assert text
    assert "Yoshiyuki" in text
