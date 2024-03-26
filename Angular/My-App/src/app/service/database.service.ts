import { Injectable } from '@angular/core';
const  sqlite3 = require('sqlite3').verbose();

let db = new sqlite3.Database('../components/film-list/db.sqlite3')
let results = db.all("SELECT * FROM main.recommend_movie")
@Injectable({
  providedIn: 'root'
})
export class DatabaseService {


  constructor() {
  }
  get_films() {
    return results
  }
}
