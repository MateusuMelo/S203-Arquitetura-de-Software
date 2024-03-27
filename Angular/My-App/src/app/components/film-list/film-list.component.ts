import {Component, OnInit} from '@angular/core';
import {FilmListService} from "../../service/film-list.service";
import {IFilms} from "../../models/i-films"


@Component({
  selector: 'app-film-list',
  templateUrl: './film-list.component.html',
  styleUrls: ['./film-list.component.scss']
})
export class FilmListComponent implements OnInit {
  films: IFilms[] = [];

  constructor(private service: FilmListService) {
  }

  ngOnInit(): void {
    this.service.getFilms().subscribe(result => this.films = ((result as any).data)
    );

  }
}
