import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { MyCardComponent } from './components/my-card/my-card.component';
import { DashboardContainerComponent} from './containers/dashboard-container/dashboard-container.component';
import { HttpClientModule } from '@angular/common/http';
import { CardsService } from './cards.service';
import { CommonModule } from '@angular/common';

@NgModule({
  declarations: [
    AppComponent,
    MyCardComponent,
    DashboardContainerComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    HttpClientModule,
    CommonModule,

  ],
  providers: [CardsService],
  bootstrap: [AppComponent]
})
export class AppModule { }
