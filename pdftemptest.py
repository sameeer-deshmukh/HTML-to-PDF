import pdfkit

isPartsAdded = False


# template names - here
templates = ['SBE', 'TECH', 'PARTS'] if isPartsAdded else ['SBE', 'TECH']

# template html file names - here
template_filenames = {'SBE': 'invoice_sbe.html', 'TECH': 'invoice_tech.html', 'PARTS': 'invoice_material.html'}
template_content = {}

# main template headings - database
template_headings = {'SBE': 'TAX INVOICE', 'TECH': 'TAX INVOICE (TECHNICIAN INVOICE)', 'PARTS': 'PAYMENT RECEIPT ON BEHALF OF SERVICE PROFESSIONAL'}

# service trade - API call ----------------------
trade = 'Plumber'

# main service description & SAC - database
service_desc = {'SBE': 'Convenience and Platform Fee', 'TECH': f'Service Charges - {trade}', 'PARTS': f'Parts Charges - {trade}'}
service_sacs = {'SBE': '999799', 'TECH': '995462'}

# reg details - database
logo_src = 'http://static.azulman-test.com/images/logo.png'
reg_company_name = 'SBE Technologies India Pvt. Ltd.'
reg_address = 'D-104, Himalaya Valley, Hindustan Colony, Amravati Road, Nagpur - 440033, Maharashtra (27)'
reg_gstin = '27AAWCS3275Q1Z6'
reg_contact_no = '+91-7387102985'

# footer juridiction & for company name text - database
footer_subject_to_juri = 'Subject to Nagpur Jurisdiction'
footer_for_company = f'For {reg_company_name}'

# notes for each page - database
note_list = {
    'SBE': ['*This is a computer-generated document. No signature is required.'],
    'TECH': ['*Under reverse charge applicability',
        '*This invoice is being generated on behalf of the Service Provider. Azulman functions as an Electronic Commerce operator in accordance with Section 9(5) of the CGST Act, 2017.',
        '*Azulman has affixed its signature to this invoice solely for the specific purpose of fulfilling its obligations as an Electronic Commerce Operator.'],
    'PARTS': ['*This is a computer-generated document. No signature is required.',
    '*Kindly ask the Service Provider to provide the original invoice for the materials that were purchased on your behalf - if available.']
}

# technician details - API call ----------------------
business_name = 'Nikhil Bandu Perker'
business_gstin = ''

# customer details - API call ----------------------
customer_name = 'Sameer Deshmukh'
customer_address = 'Joshiwadi, Gopal Nagar, Nagpur, Maharashtra, India - 440022'

# invoice & order - id & date - API call ----------------------
invoice_date = '25-Oct-2023'
invoice_no = 'INVEL2510202302'
order_date = '23-Oct-2023'
order_id = 'NGPEL2510202305'


# catalog items - API call ----------------------
service_items = [
      {'name': 'Tap Leakage', 'quantity': 1, 'rate': 182.40, 'amount': 182.40},
      {'name': 'Drainage Repair', 'quantity': 1, 'rate': 182.40, 'amount': 182.40}
      ]

# amount_breakups - API call ----------------------
amount_breakup_sbe = [
       {'name': 'Gross Amount', 'amount': 115.20, 'sign': '+'},
       {'name': 'Discount', 'amount': 0.00, 'sign': '-'},
       {'name': 'Taxable Amount', 'amount': 115.20, 'sign': '+'},
       {'name': 'GST 18%', 'amount': 20.74, 'sign': '+'},
       {'name': 'Round Off', 'amount': 0.06, 'sign': '+'},
       {'name': 'Total', 'amount': 136.00, 'sign': '+'}
]
amount_breakup_tech = [
       {'name': 'Gross Amount', 'amount': 364.80, 'sign': '+'},
       {'name': 'Discount', 'amount': 0.00, 'sign': '-'},
       {'name': 'Taxable Amount', 'amount': 364.80, 'sign': '+'},
       {'name': 'GST 18%', 'amount': 18.24, 'sign': '+'},
       {'name': 'Round Off', 'amount': 0.4, 'sign': '-'},
       {'name': 'Total', 'amount': 383.00, 'sign': '+'}
]
amount_breakup_parts = [
       {'name': 'Gross Amount', 'amount': 150.00, 'sign': '+'},
       {'name': 'Discount', 'amount': 0.00, 'sign': '-'},
       {'name': 'Taxable Amount', 'amount': 150.00, 'sign': '+'},
       {'name': 'Total', 'amount': 150.00, 'sign': '+'}
]
amount_breakup={'SBE' : amount_breakup_sbe, 'TECH' : amount_breakup_tech, 'PARTS' : amount_breakup_parts}

# - API call ----------------------
amounts_in_words={
    'SBE' : "One Hundred Thirty Six Rupees Only",
    'TECH' : "Three Hundred Eighty Three Rupees Only", 
    'PARTS' : "One Hundred Fifty Rupees Only"
}



for template in templates:

    # to change the start index of amount_breakup for each template as - 
    # for technician invoice: it is below the serice_items list and
    # for SBE and Parts invoice: it is in the same line with main service description
    amount_breakup_start_index = 1

    template_head = """
    <!DOCTYPE html>
    <html lang='en' style='height: 258mm;'>
    <head>
        <meta charset='UTF-8'>
        <meta name='viewport' content='width=device-width, initial-scale=1.0'>
        <link href='https://fonts.googleapis.com/css?family=Poppins' rel='stylesheet'>
        <style>
            *{
                box-sizing: border-box;
            }
            body{
                font-family:'Poppins'; 
                box-sizing: border-box; 
                font-size: 12px; 
                height: 258mm;
            }
            p{
                margin: 2px;
            }
            th,td {
                width: 33.33%;
            }
            .container{
                padding: 16px; 
                position: relative; 
                height: 258mm;
            }
            .field-heading{
                color: #777;
            }
            .indented-text{
            margin-left: 16px;
            }
            .header-last-col h2{
                font-size: 14px;
            }
            .float-right{
                text-align: right; 
                width: 50%; 
                float: right;
            }
            .float-left{
                text-align: left; 
                width: 50%; 
                float: left;
            }
            .customer-name,
            .customer-address,
            .business-name,
            .business-gstin{
                border-bottom: 1px solid #bfbfbf; 
                margin-bottom: 16px;
                margin-right: 10%;
            }
            .delivery-heading{
                margin-right: 10%;
                margin-botton: 4px;
            }
            .business-gstin{
                margin-bottom: 0;
            }
            .business-name{
                margin-top: 8px;
            }
            .order-date,
            .invoice-number,
            .invoice-date,
            .order-id{
                border-bottom: 1px solid #bfbfbf; 
                margin-bottom: 16px; 
                margin-left: 60%;
            }
            .header-table{
                width: 100%;
                border-bottom: 1px solid #777; 
                padding-bottom: 8px;
            }
            .gross-row{
                border-top: 1px solid #bfbfbf; 
            }
            .header-first-col{
                width: auto;
            }
            .header-mid-col{
                width: 60%;
                padding-left: 16px;
            }
            .header-last-col{
                min-width: 25%;
            }
            .first-col{
                text-align: start; 
                padding: 8px 0 8px 8px;
            }
            .mid-col{
                text-align: right;
            }
            .last-col{
                text-align: end; 
                padding: 8px 8px 8px 0;
            }
            .sub-title{
                font-size: 10px; 
                color: #777;
            }
            .order-details::after,
            .bill-details::after{
                content: '';
                display: table;
                clear: both;
            }
            .page-footer{
                position: absolute; 
                bottom: 4px;
                width: 95%;
            }
            .footer-table{
                width: 100%; 
                border-bottom: 1px solid #777;
                margin-bottom: 8px; 
                padding-bottom: 8px;
            }
            footer li{
                font-size: 8px;
                color: #777;
                list-style-type: none;
            }
        </style>
    </head>
    """

    template_body_header = f"""
        <body>
            <div class='container'>
                <header class='page-header'>
                    <table class='header-table'>
                        <tr>
                            <td class='header-first-col'>
                                <img src={logo_src} alt='azulman_logo' width='80px' height='80px'>
                            </td>
                            <td class='header-mid-col'>
                                <div class='reg-details-container' style='width: 100%;'>
                                    <div class='reg-details' style='width: 100%; line-height: 18px;'>
                                        <h3 style='margin: 2px; font-size: 18px;'>{reg_company_name}</h3>
                                        <div class='reg-address'>
                                            <p style='font-size: 12px; line-height: 18px;'>{reg_address}</p>
                                        </div>
                                        <div class='reg-gstin' style='font-size: 12px;'>
                                            <p>
                                                <span>GSTIN: {reg_gstin}</span><span class='indented-text'>Contact No: {reg_contact_no}</span>
                                            </p>
                                        </div>
                                    </div>
                                </div>
                            </td>
                            <td class='header-last-col' style='text-align: right;'>
                                <h2 style='font-family:'Poppins''>{template_headings[template]}</h2>
                            </td>
                        </tr>
                    </table>
                </header>
    """

    template_body_main = f"""
            <main>
                <div class='order-details' style='padding-top: 16px;'>
                    <div class='customer-details float-left'>
                        <div class='customer-name'>
                            <p class='field-heading'>Customer Name</p>
                            <p>{customer_name}</p>
                        </div>
                        <div class='customer-address'>
                            <p class='field-heading'>Customer Address</p>
                            <p>{customer_address}</p>
                        </div>"""

    # to add a title "DELIVERY SERVICE PROVIDER" for Parts receipt only
    if template == 'PARTS':
        template_body_main += f"""
            <div class='delivery-heading'>
                <p><h3>DELIVERY SERVICE PROVIDER<h3><p>
            </div>
            """
    # to add "business name"
    if template in ['TECH', 'PARTS']:
        template_body_main += f"""
                            <div class='business-name'>
                                <p class='field-heading'>Business Name</p>
                                <p>{business_name}</p>
                            </div>"""
    # to add "business gstin"
    if template == 'TECH':
        template_body_main += f"""    
                            <div class='business-gstin'>
                                <p class='field-heading'>Business GSTIN</p>
                                <p>{business_gstin}</p>
                            </div>
                            """

    template_body_main += f"""
                        </div>
                        <div class='invoice-details float-right'>
                                <div class='invoice-date'>
                                    <p class='field-heading'>Invoice Date</p>
                                    <p>{invoice_date}</p>
                                </div>
                                <div class='invoice-number'>
                                    <p class='field-heading'>Invoice No.</p>
                                    <p>{invoice_no}</p>
                                </div>
                                <div class='order-date'>
                                    <p class='field-heading'>Order Date</p>
                                    <p>{order_date}</p>
                                </div>
                                <div class='order-id'>
                                    <p class='field-heading'>Order ID</p>
                                    <p>{order_id}</p>
                                </div>
                            </div>
                    </div>"""

    template_body_main_bill_details = """
                <div class='bill-details' style='margin-top: 16px; position: static;'>
                    <div class='bill-details-headline'>
                        <table style='width: 100%; border-collapse: collapse;'>
                            <tr style='background: #f5f5f5; font-family: Poppins;'>
                                <th class='first-col'>Description of Items</th>
                                <th class='mid-col'></th>
                                <th class='last-col'>Amount</th>
                            </tr>
                        </table>
                    </div>
                    <div class='bill-details-main'>
                        <table style='width: 100%; border-collapse: collapse;'>
                        """

    
    template_body_main_bill_details += f"""
        <tr>
            <td class='first-col'><p>{service_desc[template]}</p>
            """
    # to "skip SAC" for Parts Receipt
    if template != 'PARTS':
        template_body_main_bill_details += f"""<p class='sub-title'>SAC: {service_sacs[template]}</p>"""
            
    template_body_main_bill_details += f"""
            </td>"""
    # to add extra columns to not start "Gross Total" from the same line in Technician Invoice as
    # main service description because we are adding "service_items" below main service description
    # and then adding "amount_breakup"
    if template == 'TECH':
        template_body_main_bill_details +="""
                <td class='mid-col'></td>
                <td class='last-col'></td>
            </tr>
                """
    else:
        template_body_main_bill_details +=f"""
                <td class='mid-col'>{amount_breakup[template][0]['name']}</td>
                <td class='last-col'>{'{0:.2f}'.format(amount_breakup[template][0]['amount'])}</td>
            </tr>
                """
    if template == 'TECH':
        # to set to start the "amount_breakup" loop to start from "Gross Amount" as
        # we have not added it in the main service description line because it is
        # "technician invoice"
        amount_breakup_start_index = 0   

        # to add "service_list" in "technician invoice"
        for service_item in service_items:
            template_body_main_bill_details += f"""
                <tr>
                    <td class='first-col'>&nbsp;&nbsp;&nbsp;&nbsp;{service_item['name']}<span class='sub-title'>(Qty: {service_item['quantity']})</span></td>
                    <td class='mid-col'></td>
                    <td class='last-col'>₹ {'{0:.2f}'.format(service_item['amount'])}</td>
                </tr>
                """
    
    # to add border-top to "gross total" row in "technician invoice"
    template_body_main_bill_details += """<tr class='gross-row'>""" if template == 'TECH' else """<tr>"""

    # to add "amount_breakup"
    for amount_row in amount_breakup[template][amount_breakup_start_index:-1]:
        template_body_main_bill_details += f"""
                <td class='first-col'></td>
                <td class='mid-col'>{amount_row['name']}</td>
                <td class='last-col'>""" 
        # to ignore +ve sign and add -ve sign when we subtract the amount in case of -
        # "discount" and "Round-off"
        if amount_row['sign'] == '-':
            template_body_main_bill_details += f"""
            - ₹ {'{0:.2f}'.format(amount_row['amount'])}</td>
            </tr>
            """
        else:
            template_body_main_bill_details += f"""
            ₹ {'{0:.2f}'.format(amount_row['amount'])}</td>
            </tr>
            """

    template_body_main_bill_details += f"""</table>
                    </div>
                    <div class='bill-details-footer'>
                        <table style='width: 100%; border-collapse: collapse;'>
                            <tr style='background: #f5f5f5;'>
                                <th class='first-col'>Total</th>
                                <th class='mid-col'></th>
                                <th class='last-col'>₹ {'{0:.2f}'.format(amount_breakup[template][-1]['amount'])}</th>
                            </tr>
                            <tr>
                                <th></th><th></th><th class='last-col'>{amounts_in_words[template]}</th>
                            </tr>
                        </table>
                    </div>
                </div>
            </main>
        """

    template_body_footer = f"""
                <footer class='page-footer'>
                    <table class='footer-table'>
                        <tr>
                            <td>
                                <p>{footer_subject_to_juri}</p>
                            </td>
                            <td style='text-align: right;'>
                                <p><strong>{footer_for_company}</strong></p>
                            </td>
                        </tr>
                    </table>"""

    # to display the footer notes
    for i in range(len(note_list[template])):
        template_body_footer += f"""<li>{note_list[template][i]}</li>"""

    template_body_footer += """
                </footer>
            </div>
        </body>
        </html>
    """

    # to merge all the HTML strings
    template_content[template] = template_head + template_body_header + template_body_main + template_body_main_bill_details + template_body_footer

# to pass the list of filenames in pdfkit.from_file()
files = []

# to loop through each template - get each filename 
# - get content for each file - create the file and write a content to the file
for template in templates:
    with open(template_filenames[template], 'w') as file:
        files.append(template_filenames[template])
        file.write(template_content[template])


config = pdfkit.configuration(wkhtmltopdf='/usr/local/bin/wkhtmltopdf')
options = {
    'page-size': 'A5',
    'orientation': 'portrait',
    'margin-top': '0mm',
    'margin-right': '0mm',
    'margin-bottom': '0mm',
    'margin-left': '0mm'
}
pdfkit.from_file(files, 'multi_page_with_var_final.pdf', options=options, configuration=config)

