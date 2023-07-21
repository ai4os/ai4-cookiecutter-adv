"""Module for defining custom API response parsers and content types.
"""
import logging
from fpdf import FPDF
from . import config

logger = logging.getLogger(__name__)
logger.setLevel(config.log_level)


def json_response(result, **extra_values):
    """Converts the prediction or training results into json return format.

    Arguments:
        result -- Result value from predict call, expected either dict or str
          (see https://docs.deep-hybrid-datacloud.eu/projects/deepaas/en/stable/user/v2-api.html).
        extra_values -- Not used, added for illustration purpose.

    Returns:
        Converted values into json dictionary format.
    """
    logger.debug(f"Response result: {result}")
    logger.debug(f"Response result, type: {type(result)}")
    logger.debug(f"Response options: {extra_values}")
    
    if isinstance(result, dict) or isinstance(result, str):
        return result
    else:
        return {"result": str(result)}


# EXAMPLE FUNCTION on how to return e.g. PDF document with the output of the predict() method
# = HAVE TO MODIFY FOR YOUR NEEDS =
def pdf_response(result, **extra_values):
    """Converts the prediction or training results into PDF format.

    Arguments:
        result -- Result value from predict call, normally expected either dict or str
          (see https://docs.deep-hybrid-datacloud.eu/projects/deepaas/en/stable/user/v2-api.html).
        extra_values -- input parameter dictionary

    Returns:
        Converted values into pdf buffer format.
    """

    logger.debug(f"Response result  (PDF): {result}")
    logger.debug(f"Response result, type: {type(result)}")
    logger.debug(f"Response options (PDF): {extra_values}")

    # 1. create BytesIO object
    buffer = io.BytesIO()
    buffer.name = 'output.pdf'
    # 2. write the output of the predict() method in the buffer
    #    For the proper PDF document, you may use:
    #    * matplotlib for images
    #    * fPDF2 for text documents (pip3 install fPDF2)
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('helvetica', size=12)
    # in this EXAMPLE we also add input parameters
    print_out = {"input": str(extra_values),
                 "predictions": str(result)
                }
    pdf.multi_cell(w=0, txt=str(print_out).replace(',',',\n'))
    pdf_output = pdf.output(dest='S')
    buffer.write(pdf_output)
    # 3. rewind buffer to the beginning
    buffer.seek(0)
    
    return buffer


content_types = {
    "application/json": json_response,
    "application/pdf": pdf_response,
}

