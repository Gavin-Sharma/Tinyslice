const items = [
    { 
      name: "Apple", 
      price: 1.99,
      item_id: '0' 
    },
    { 
      name: "Orange", 
      price: 1.25,
      item_id: '1'
    },
    { 
      name: "Pear", 
      price: 2.99,
      item_id: '2'
    },
    { 
      name: "Grape", 
      price: 3.99,
      item_id: '3'
    }
  ]

let list_id = [
  { 
    title: "Grocery List 1", 
    id: 0
  }
]

let user_items = [
  [
    { 
      name: "Pear", 
      price: 2.99,
      item_id: '2'
    }
  ]
]

const newlist_button = document.getElementById('newlist-button')

// getting different divs in html
const second_header_div = document.getElementById('second-header')
const list_title_div = document.getElementById('list-title')
const addgrocery_list_div = document.getElementById('add-grocery-list')
const next_button = document.getElementById('button-next')
const add_button_div = document.getElementById('button-group')
const viewing_list_div = document.getElementById('viewing-list')

let page_state = 'home';

page_shown();

// changes the page from home -> request title
function page_shown() {
  if (page_state == 'home') {
    // Displays the home page
    list_title_div.style.display = 'none';
    addgrocery_list_div.style.display = 'none';
    viewing_list_div.style.display = 'none';
    request_list_title();

  }  else if (page_state == 'adding items') {
    // Displays the page where user will add items to the list
    addgrocery_list_div.style.display = 'none';
    list_title_div.style.display = 'flex';
    request_list_title();

  } else if (page_state == 'viewing list') {
    // Displays the page where user is viewing the list of items
    viewing_list_div.style.display = 'none';

    list_title_div.style.display = 'flex';
    request_list_title();
  }
  
}

// Asks the user to enter the title for the list
function request_list_title () {
  document.getElementById('newlist-title').value = '';
  newlist_button.addEventListener('click', (evt) => {
    page_state = 'request title'
    second_header_div.hidden = true;
    list_title_div.style.display = 'flex';
    adding_items();
  }, {once: true})
}

// Displays the list of items stored in the system with a specific price
function adding_items() {
  next_button.addEventListener('click', (evt) => {
    addgrocery_list_div.style.display = 'flex';
    list_title_div.style.display = 'none';
    let title = document.getElementById('newlist-title').value;
    save_title(title);
  }, {once: true})

  newlist_button.addEventListener('click', (evt) => {
    page_state = 'adding items'
    page_shown();
  }, {once: true})
}

// Saves the user's inputted title 
function save_title(title) {
  let id = list_id.length;
  list_id.push({title, id})
  display_title(title, id)
}

// Displays the list of list titles in the side nav
function display_title(title, id) {
  const grocery_list = document.querySelector('#created-lists')
  const grocery_title = `<li><p id='${id}'>${title}</p></li>`
  grocery_list.insertAdjacentHTML('beforeend', grocery_title)
  user_items.push([]);
  add_button(id);
  view_list();
}

// Veiw the selected grocery list title on the side nav
function view_list() {
  const grocery_list = document.getElementById('created-lists')
  grocery_list.addEventListener('click', (evt) => {
    for (created_lists of list_id) {
      if (evt.target.id == created_lists.id) {
        addgrocery_list_div.style.display = 'none';
        show_list(evt.target.id);
      }
    }
  })
}

// Showing the list of items in the selected title
function show_list(selected_id) { 
  let total_cost = 0.0;

  viewing_list_div.style.display = 'flex';
  const list_grocery = user_items[selected_id]
  const view_items = document.querySelector('#view-items')
  const view_prices = document.querySelector('#view-prices')
  for (const items of list_grocery) {
    const insert_items = `<li id="item-shown">${items.name}</li>`
    const insert_price = `<li id="item-shown">$${items.price}</li>`
    view_items.insertAdjacentHTML('beforeend', insert_items)
    view_prices.insertAdjacentHTML('beforeend', insert_price)
    total_cost = total_cost + items.price;
  }
  const remove_items_shown = document.getElementById('item-shown')
  const insert_cost = `<p id="cost-total">Total Cost: $${total_cost}</p>`
  const display_cost = document.getElementById('display-cost')
  display_cost.insertAdjacentHTML('beforeend', insert_cost)

  newlist_button.addEventListener('click', (evt) => {
    page_state = 'viewing list'
    remove_items_shown.remove();
    page_shown();
  })
}

// Adding event listener to the "add" buttons and adds the item when the add button is clicked
function add_button(selected_id) {
  add_button_div.addEventListener('click', (evt) => {
    for (const grocery_item of items) {
      if (evt.target.id == grocery_item.item_id) {
        user_items[selected_id].push(grocery_item)
      }
    }
  })
}
