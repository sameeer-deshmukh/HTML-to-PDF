logo_src = 'http://static.azulman-test.com/images/logo.png'
reg_company_name = 'SBE Technologies India Pvt. Ltd.'
reg_address = 'D-104, Himalaya Valley, Hindustan Colony, Amravati Road, Nagpur - 440033, Maharashtra (27)'
reg_gstin = '27AAWCS3275Q1Z6'

template_heading = 'TAX INVOICE'

customer_name = 'Sameer Deshmukh'
customer_address = 'Joshiwadi, Gopal Nagar, Nagpur, Maharashtra, India - 440022'

invoice_date = '25-Oct-2023'
invoice_no = 'INVEL2510202302'
order_date = '23-Oct-2023'

footer_subject_to_juri = 'Subject to Nagpur Jurisdiction'
footer_for_company = f'For {reg_company_name}'

footer_message_list = [
    'This is a computer-generated document. No signature is required.'
]

tax_invoice_template_head = """
<!DOCTYPE html>
<html lang="en" style="height: 258mm;">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
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
        .business-gstin{
            margin-bottom: 0;
        }
        .business-name{
            margin-top: 8px;
        }
        .order-date,
        .invoice-number,
        .invoice-date{
            border-bottom: 1px solid #bfbfbf; 
            margin-bottom: 16px; 
            margin-left: 60%;
        }
        .header-table{
            width: 100%;
            border-bottom: 1px solid #777; 
            padding-bottom: 16px;
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
        .order-details::after,
        .bill-details::after{
            content: '';
            display: table;
            clear: both;
        }
        .page-footer{
            position: absolute; 
            bottom: 32px;
            width: 97%;
        }
        .footer-table{
            width: 100%; 
            border-bottom: 1px solid #777;
            margin-bottom: 8px; 
            padding-bottom: 8px;
        }
        footer li{
            font-size: 10px;
            color: #777;
        }
    </style>
</head>
"""

tax_invoice_template_body_header = f"""
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
                                            GSTIN: {reg_gstin}
                                        </p>
                                    </div>
                                </div>
                            </div>
                        </td>
                        <td class='header-last-col' style='text-align: right;'>
                            <h2 style='font-family:'Poppins''>{template_heading}</h2>
                        </td>
                    </tr>
                </table>
            </header>
"""

tax_invoice_template_body_main = f"""
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
                    </div>
                    <div class="business-name">
                        <p class="field-heading">Business Name</p>
                        <p>Nikhil Bandu Perker</p>
                    </div>
                    <div class="business-gstin">
                        <p class="field-heading">Business GSTIN</p>
                        <p></p>
                    </div>
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
                    </div>
            </div>
            <div class="bill-details" style="margin-top: 16px; position: static;">
                <div class="bill-details-headline">
                    <table style="width: 100%; border-collapse: collapse;">
                        <tr style="background: #f5f5f5; font-family: Poppins;">
                            <th class="first-col">Description of Items</th>
                            <th class="mid-col"></th>
                            <th class="last-col">Amount</th>
                        </tr>
                    </table>
                </div>
                <div class="bill-details-main">
                    <table style="width: 100%; border-collapse: collapse;">
                        <tr>
                            <td class="first-col"><p>Serivce Charges - Plumber</p><p style="font-size: 10px; color: #777;">SAC: 999799 
                            </p></td>
                            <td class="mid-col"></td>
                            <td class="last-col"></td>
                        </tr>
                        <tr>
                            <td class="first-col">&nbsp;&nbsp;&nbsp;&nbsp;Tap Leakage</td>
                            <td class="mid-col"></td>
                            <td class="last-col">₹ 182.40</td>
                        </tr>
                        <tr>
                            <td class="first-col">&nbsp;&nbsp;&nbsp;&nbsp;Blockage/Drainage Repair</td>
                            <td class="mid-col"></td>
                            <td class="last-col">₹ 182.40</td>
                        </tr>
                        <tr>
                            <td class="first-col">&nbsp;&nbsp;&nbsp;&nbsp;Tap Leakage</td>
                            <td class="mid-col"></td>
                            <td class="last-col">₹ 182.40</td>
                        </tr>
                        <tr>
                            <td class="first-col">&nbsp;&nbsp;&nbsp;&nbsp;Blockage/Drainage Repair</td>
                            <td class="mid-col"></td>
                            <td class="last-col">₹ 182.40</td>
                        </tr>
                        <tr>
                            <td class="first-col">&nbsp;&nbsp;&nbsp;&nbsp;Tap Leakage</td>
                            <td class="mid-col"></td>
                            <td class="last-col">₹ 182.40</td>
                        </tr>
                        <tr class="gross-row">
                            <td class="first-col"></td>
                            <td class="mid-col">Gross Amount</td>
                            <td class="last-col">₹ 364.80</td>
                        </tr>
                        <tr>
                            <td class="first-col"></td>
                            <td class="mid-col">Discount</td>
                            <td class="last-col">- ₹ 0.00</td>
                        </tr>
                        <tr>
                            <td class="first-col"></td>
                            <td class="mid-col">Taxable Amount</td>
                            <td class="last-col">₹ 364.80</td>
                        </tr>
                        <tr>
                            <td class="first-col"></td>
                            <td class="mid-col">GST 18%</td>
                            <td class="last-col">₹ 18.24</td>
                        </tr>
                        <tr>
                            <td class="first-col"></td>
                            <td class="mid-col">Round Off</td>
                            <td class="last-col">- ₹ 0.04</td>
                        </tr>
                    </table>
                </div>
                <div class="bill-details-footer">
                    <table style="width: 100%; border-collapse: collapse;">
                        <tr style="background: #f5f5f5;">
                            <th class="first-col">Total</th>
                            <th class="mid-col"></th>
                            <th class="last-col">₹ 383.00</th>
                        </tr>
                        <tr>
                            <th></th><th></th><th class="last-col">Three Hundred Three Rupees Only</th>
                        </tr>
                    </table>
                </div>
            </div>
        </main>
"""

tax_invoice_template_body_footer = f"""
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

for msg in footer_message_list:
    tax_invoice_template_body_footer += f"""<li>{msg}</li>"""

tax_invoice_template_body_footer += """
            </footer>
        </div>
    </body>
    </html>
"""