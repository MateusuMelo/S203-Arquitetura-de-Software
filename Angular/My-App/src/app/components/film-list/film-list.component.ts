import {Component, OnInit} from '@angular/core';
import {FilmListService} from "../../service/film-list.service";
import {IFilms} from "../../models/i-films";
import {DatabaseService} from "../../service/database.service";

@Component({
  selector: 'app-film-list',
  templateUrl: './film-list.component.html',
  styleUrls: ['./film-list.component.scss']
})
export class FilmListComponent implements OnInit{
  dataset = new DatabaseService()
  films :IFilms[] = [];
  constructor(private service:FilmListService) {
  }
  ngOnInit():void {

    this.films = [
      {id:18,title:'12 Angry Men', gen:'Crime, Drama'},
      {id:19,title:'12 Years a Slave', gen:'Drama, History'},
      {id:20,title:'A Beautiful Mind', gen:'Biography, Drama'},
    ]
    //console.log(this.dataset.get_films())

    this.films = []
    for (let i of this.films){
      console.log(i.id);
      console.log(i.title);
      console.log(i.gen);
    }
  }
}
