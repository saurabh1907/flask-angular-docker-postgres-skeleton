import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import {HomeComponent} from './home/home.component';
import {AboutMeComponent} from './about/about-me.component';
import {ViewBlogComponent} from './view-blog/view-blog.component';
import {AddBlogComponent} from './add-blog/add-blog.component';

const routes: Routes = [
  { path: '', redirectTo: '/home', pathMatch: 'full' }, // default route
  { path: 'home', component: HomeComponent },
  { path: 'about', component: AboutMeComponent },
  { path: 'blogs/:id', component: ViewBlogComponent },
  { path: 'add-blog', component: AddBlogComponent },
  { path: '**', redirectTo: '404', pathMatch: 'full' },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule {}
