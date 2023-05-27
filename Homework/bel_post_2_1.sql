--
-- PostgreSQL database dump
--

-- Dumped from database version 15.2
-- Dumped by pg_dump version 15.2

-- Started on 2023-05-27 18:00:33

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 215 (class 1259 OID 16676)
-- Name: izdaniya; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.izdaniya (
    idx_izdaniya integer NOT NULL,
    vid_izdaniya character varying(40),
    name_izdaniya character varying(100),
    price money
);


ALTER TABLE public.izdaniya OWNER TO postgres;

--
-- TOC entry 214 (class 1259 OID 16669)
-- Name: podpiski; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.podpiski (
    kod_poluchatelya integer NOT NULL,
    idx_izdaniya integer NOT NULL,
    srok_podpiski integer,
    month integer,
    year integer,
    CONSTRAINT podpiski_month_check CHECK (((month > 0) AND (month < 13))),
    CONSTRAINT podpiski_srok_podpiski_check CHECK (((srok_podpiski = 1) OR (srok_podpiski = 3) OR (srok_podpiski = 6)))
);


ALTER TABLE public.podpiski OWNER TO postgres;

--
-- TOC entry 216 (class 1259 OID 16681)
-- Name: poluchatel; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.poluchatel (
    kod_poluchatelya integer NOT NULL,
    fio character varying(100),
    address character varying(100)
);


ALTER TABLE public.poluchatel OWNER TO postgres;

--
-- TOC entry 3333 (class 0 OID 16676)
-- Dependencies: 215
-- Data for Name: izdaniya; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.izdaniya (idx_izdaniya, vid_izdaniya, name_izdaniya, price) FROM stdin;
777	Magazine	Nauka i technika	$200.00
888	Newspaper	Pravda	$100.00
999	Newspaper	Utro i vecher	$120.00
666	Magazine	V mire zverey	$150.00
555	Magazine	U reki	$160.00
444	Magazine	Vokrug sveta	$210.00
\.


--
-- TOC entry 3332 (class 0 OID 16669)
-- Dependencies: 214
-- Data for Name: podpiski; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.podpiski (kod_poluchatelya, idx_izdaniya, srok_podpiski, month, year) FROM stdin;
1	777	3	3	2023
2	888	6	3	2023
3	999	6	2	2023
\.


--
-- TOC entry 3334 (class 0 OID 16681)
-- Dependencies: 216
-- Data for Name: poluchatel; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.poluchatel (kod_poluchatelya, fio, address) FROM stdin;
1	Иванов Иван Иванович	Минск, ул. Ленина, д.5, кв.13
2	Петров Петр Петрович	Минск, ул. Ленина, д.5, кв.14
3	Васильев Василий Васильевич	Минск, ул. Ленина, д.5, кв.15
4	Шварценеггер Арнольд Сталлонович	Минск, ул. Красная площадь, д.1, кв.1
5	Мустахимова Светлана Арсеновна	Минск, 1-ый Грайвороновский проезд, д.1 кв.2
6	Исмаилов Аганес Вартанович	Минск, ул. Красногвардейская, д.4, кв.17
\.


--
-- TOC entry 3185 (class 2606 OID 16680)
-- Name: izdaniya izdaniya_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.izdaniya
    ADD CONSTRAINT izdaniya_pkey PRIMARY KEY (idx_izdaniya);


--
-- TOC entry 3183 (class 2606 OID 16675)
-- Name: podpiski podpiski_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.podpiski
    ADD CONSTRAINT podpiski_pkey PRIMARY KEY (kod_poluchatelya, idx_izdaniya);


--
-- TOC entry 3187 (class 2606 OID 16685)
-- Name: poluchatel poluchatel_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.poluchatel
    ADD CONSTRAINT poluchatel_pkey PRIMARY KEY (kod_poluchatelya);


--
-- TOC entry 3188 (class 2606 OID 16691)
-- Name: podpiski podpiski_idx_izdaniya_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.podpiski
    ADD CONSTRAINT podpiski_idx_izdaniya_fkey FOREIGN KEY (idx_izdaniya) REFERENCES public.izdaniya(idx_izdaniya);


--
-- TOC entry 3189 (class 2606 OID 16686)
-- Name: podpiski podpiski_kod_poluchatelya_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.podpiski
    ADD CONSTRAINT podpiski_kod_poluchatelya_fkey FOREIGN KEY (kod_poluchatelya) REFERENCES public.poluchatel(kod_poluchatelya);


-- Completed on 2023-05-27 18:00:33

--
-- PostgreSQL database dump complete
--

