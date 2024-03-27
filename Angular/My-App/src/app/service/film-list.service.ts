import {Injectable} from '@angular/core';
import {HttpClient} from "@angular/common/http";

@Injectable({
  providedIn: 'root'
})
export class FilmListService {
  uri = "http://localhost:3000/films"

  constructor(private http: HttpClient) {
  }

  getFilms() {
    return this.http.get(this.uri);
  }
}
