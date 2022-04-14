/*
    Assumptions:  
  	    We have a site with a simple form where a user can enter data required to create a Supplier Invoice.
        We have a REST API which allows us POST supplier invoice data to a backend. 
    Story:
  	    As an Activity Tracker, I need to capture the details of a Supplier Invoice
        so that a Supplier can be paid for services rendered. 
    Your Goal: 
  	    Get the user supplied data, and submit it ot the backend, asynchronously: 
            - Send the Supplier Invoice
            - Wait for a response
            - Process the response - consider both success and error conditions.   
    Bonus: 
        What does the user see when all this happens? How do they know it's done?  
*/

const supplierInvoicePostingEndpoint = "https://thisIsATestAPICall";
const regularPost = {
    method: 'POST',
    headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }
}
// Mock error reporting functions
const reportInvoicePostingError = (error) => {};
const reportInternalDBError = (error) => {};

// Mock load DB function
const loadInvoiceFromDB = () => new Promise((resolve,reject) => setTimeout(resolve(new SupplierInvoice()), 2000));

// User interaction assumed functions
const showProgressBar = () => { /*  Show the indeterminate progress bar to users  */ };
const hideProgressBar = () => { /*  Hide the progress bar  */ };
const showPostingSuccess = () => { /*  Show posting success to users  */ }

// Main Supplier Invoice class
class SupplierInvoice {

    // Implement Me!
}

// Main Form JS
function onSendInvoiceForPayment() {
    
    // Implement Me!
}