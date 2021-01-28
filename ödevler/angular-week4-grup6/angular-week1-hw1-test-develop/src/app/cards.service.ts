import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { Card } from './card.model';


@Injectable({
  providedIn: 'root'
})
export class CardsService {

  cards : Card[];

  url = "https://jsonplaceholder.typicode.com/comments";


  constructor(private http: HttpClient) {}
  getAllCard(): Observable<any>{
  return this.http.get<Card[]>(this.url)
  }
}
